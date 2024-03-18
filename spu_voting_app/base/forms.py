from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreationFormCustomized(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email']
