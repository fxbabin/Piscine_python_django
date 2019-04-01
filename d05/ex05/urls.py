from django.urls import path

from .views import populate, display, remove

urlpatterns = [
    path('ex05/populate/', populate, name='ex05_populate'),
    path('ex05/display/', display, name='ex05_display'),
    path('ex05/remove/', remove, name='ex05_remove'), #useful to test exercice
]