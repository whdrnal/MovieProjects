from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("first_name", "username", "password1", "password2", "email")


class FindUsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'email']



