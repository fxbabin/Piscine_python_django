from django.db import models
from django import forms

# Create your models here.
class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(required = True, widget=forms.PasswordInput, initial='')