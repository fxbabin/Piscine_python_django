from django.urls import path

from .views import home, sign_in, sign_out, sign_up, delete_user

urlpatterns = [
    path('', home, name='home'),
    path('sign_in/', sign_in, name='home'),
    path('sign_out/', sign_out, name='home'),
    path('sign_up/', sign_up, name='home'),
    path('delete/', delete_user, name='home'),
]