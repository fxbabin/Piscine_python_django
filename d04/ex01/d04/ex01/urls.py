from django.urls import path

from .views import homePageView, djangoPageView, affichagePageView, templatesPageView

urlpatterns = [
    path('ex01/django', djangoPageView, name='home'),
    path('ex01/affichage', affichagePageView, name='ho'),
    path('ex01/templates', templatesPageView, name='home'),
]