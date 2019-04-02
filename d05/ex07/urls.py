from django.urls import path

from .views import populate, display, update, delete

urlpatterns = [
    path('ex07/populate/', populate, name='ex07_populate'),
    path('ex07/display/', display, name='ex07_display'),
    path('ex07/update/', update, name='ex07_update'), #useful to test exercice
    path('ex07/delete/', delete, name='ex07_delete'),
]