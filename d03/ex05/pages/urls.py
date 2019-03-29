# pages/urls.py
from django.urls import path

from .views import homePageView, helloPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('helloworld', helloPageView, name='helloworld')
]