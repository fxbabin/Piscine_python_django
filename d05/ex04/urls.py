from django.urls import path

from .views import init, populate, display, remove

urlpatterns = [
    path('ex04/init/', init, name='ex04_init'),
    path('ex04/populate/', populate, name='ex04_populate'),
    path('ex04/display/', display, name='ex04_display'),
    path('ex04/remove/', remove, name='ex04_remove'),
]