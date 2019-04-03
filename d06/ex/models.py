from django.db import models
from django import forms

class Tip(models.Model):
    contenu = models.TextField()
    auteur = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)