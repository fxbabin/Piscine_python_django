from django.urls import path

from .views import formPageView

urlpatterns = [
    path('ex02/', formPageView, name='home'),
]