from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team

class UserRegistrationForm(UserCreationForm):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'team']
