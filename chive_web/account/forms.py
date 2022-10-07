from django.contrib.auth.forms import UserCreationForm
#from .models import User
from .models import User
from django import forms


class RegisterFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']