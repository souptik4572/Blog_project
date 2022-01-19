from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()
     class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name',]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    