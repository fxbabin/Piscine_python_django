from django.urls import path

from .views import populate, init, delete, display, update

urlpatterns = [
    path('ex06/populate/', populate, name='ex06_populate'),
    path('ex06/init/', init, name='ex06_display'),
    path('ex06/delete/', delete, name='ex06_delete'), #useful to test exercice
    path('ex06/display/', display, name='ex06_display'),
    path('ex06/update/', update, name='ex06_update'),
]