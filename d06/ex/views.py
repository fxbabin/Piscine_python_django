from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
import random

from django.contrib import auth
from .forms import LoginForm

# Create your views here.
def home(request):
    if request.COOKIES.get('mycookie'):
        username = request.COOKIES['mycookie']
        response = render(request, 'home.html', {'username': username})
    else:
        username = random.choice(settings.USERS)
        response = render(request, 'home.html', {'username': username})
        response.set_cookie('mycookie', username, max_age = settings.SESSION_COOKIE_AGE)
    return (response)

def login(request):
    if request.method == "POST":
        print('ed')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user and user.is_active:
                auth.login(request, user)
                print('ff')
                return redirect('/')
            else:
                form._errors['username'] = ['This user doesn\'t exists']
    else:
        print('ffe')
        form = LoginForm()
    print('ffx')
    return render(request, 'login.html', {'form', form})

#signup ???
# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = auth.authenticate(username=username,
#                                      password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return redirect('/')
#             else:
#                 form._errors['username'] = ['This user doesn\'t exists']
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form', form})



def logout(request):
    auth.logout(request)
    return redirect('/')

#def inscription(request):

#def connexion(request):


# Create users
################

# from django.contrib.auth.models import User
# u = User(username='toto', password="mysecretpassword")
# u.username
# u.password #non hashed password
# u = User.objects.create_user('toto', None, 'mysecretpassword')
# u.username
# u.password

# User session
#################

#./manage.py createsuperuser
#toto
#email
#password

    # if request.method == "POST":
    #     cookie = request.POST.get('text', None)

    #     request.COOKIES['mycookie'] = cookie
    #     response = render(request, 'home.html')

    #     response.set_cookie('mycookie', cookie, max_age = settings.SESSION_COOKIE_AGE)
    #     return response

    # return render(request, 'home.html')

# def sign_in(request):
#     users = MyUser.objects.all()
#     if (request.method == "POST"):
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = SignInForm()
#         else:
#             form =  SignInForm()
#         return render(request, 'ex/form.html', {'users' : users,
#                                             'form': form })

# def sign_up(request):
#     if (request.method == "POST"):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             password_verif = form.cleaned_data["password_verif"]
#             if password == password_verif:
#                 user = auth.authenticate(username=username, 
#                                         password=password) 
#                 if user and user.is_active:  # Si l'objet renvoyé n'est pas None,  par défaut is_active est False
#                     auth.login(request, user)  # nous connectons l'utilisateur
#                 else: # sinon une erreur sera affichée
#                     form._errors["username"] = ["This user doesn't exist."]
#             else:
#                 form._errors["password"] = ["les mots de passe ne sont pas semblables"]
#     else:
#         form = SignUpForm()
# return render(request, 'ex/form.html', {'form': form })