from django.urls import path

from .views import home, login

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='home'),
]