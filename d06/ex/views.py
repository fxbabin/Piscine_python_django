from django.shortcuts import render, HttpResponse
from django.conf import settings
import random

# Create your views here.
def home(request):
    if request.COOKIES.get('mycookie'):
        user_name = request.COOKIES['mycookie']
        response = render(request, 'home.html', {'user_name': user_name})
    else:
        user_name = random.choice(settings.USERS)
        response = render(request, 'home.html', {'user_name': user_name})
        response.set_cookie('mycookie', user_name, max_age = settings.SESSION_COOKIE_AGE)
    return (response)

#def inscription(request):

#def connexion(request):