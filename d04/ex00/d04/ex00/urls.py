from django.urls import path

from .views import homePageView, testPageView

urlpatterns = [
    path('', testPageView, name='home'),
]