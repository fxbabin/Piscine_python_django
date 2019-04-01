from django.urls import path

from .views import init, populate, delete, display

urlpatterns = [
    path('ex02/init/', init, name='ex02_init'),
    path('ex02/populate/', populate, name='ex02_populate'),
    path('ex02/display/', display, name='ex02_display'),
    path('ex02/delete/', delete, name='ex02_delete'), #useful to test exercice
]