# pages/urls.py
from django.urls import path

from .views import helloPageView

urlpatterns = [
    path('helloworld', helloPageView, name='helloworld')
]