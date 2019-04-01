from django.urls import path

from .views import init

urlpatterns = [
    path('ex00/init/', init, name='home'),
]