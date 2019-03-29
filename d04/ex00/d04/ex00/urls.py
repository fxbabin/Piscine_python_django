from django.urls import path

from .views import homePageView, testPageView

urlpatterns = [
    path('ex00', testPageView, name='home'),
]