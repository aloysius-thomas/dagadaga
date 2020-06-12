from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = {
            "username",
            "first_name",
            "last_name",
            "phone",
            "email",
        }
