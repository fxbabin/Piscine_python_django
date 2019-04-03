from django import forms
from ex.models import Tip

class SignInForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password_verif = forms.CharField(required=True, widget=forms.PasswordInput)

class DeleteForm(forms.Form):
    username = forms.CharField(required=True)

class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['contenu']