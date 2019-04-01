from django.urls import path

from .views import populate, delete, display

urlpatterns = [
    path('ex03/populate/', populate, name='ex03_populate'),
    path('ex03/display/', display, name='ex03_display'),
    path('ex03/delete/', delete, name='ex03_delete'), #useful to test exercice
]