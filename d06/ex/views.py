from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import random

from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignInForm, SignUpForm, DeleteForm, TipForm
from .models import Tip

# Create your views here.
def home(request):

    if request.method == "POST":
            form = TipForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['contenu']
                tip = Tip(contenu = content, auteur = request.user.username)
                tip.save()
                form = TipForm()
    else:
        form = TipForm()
    tips = Tip.objects.all()
    if request.COOKIES.get('mycookie'):
        username = request.COOKIES['mycookie']
        response = render(request, 'home.html', {'username': username, 'form': form, 'tips': tips})
    else:
        username = random.choice(settings.USERS)
        response = render(request, 'home.html', {'username': username, 'form': form, 'tips': tips})
        response.set_cookie('mycookie', username, max_age = settings.COOKIE_AGE)
    return (response)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                form._errors['username'] = ['This user doesn\'t exists']
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_verif = form.cleaned_data['password_verif']

            if password == password_verif:
                if username_present(username):
                    form._errors['username'] = ['This user already exists']
                    return render(request, 'sign_up.html', {'form': form})
                u = User.objects.create_user(username, None, password)
                u.save()
            else:
                form._errors['password'] = ['passwords differs']
                return render(request, 'sign_up.html', {'form': form})
            user = auth.authenticate(username=username,
                                     password=password)
            auth.login(request, user)
            return render(request, 'home.html', {'username': username})
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_out(request):
    auth.logout(request)
    return redirect('/')

def delete_user(request):
    users = User.objects.all()
    print(users)
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            u = User.objects.get(username = username)
            u.delete()
            return render(request, 'home.html')
    else:
        form = DeleteForm()
    return render(request, 'delete.html', {'form': form})      
