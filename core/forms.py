from django import forms
from django.contrib.auth.models import User
from .models import Service


class RegisterForm(forms.ModelForm):
    '''
        register form for user
    '''
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'service_name',
            'service_description',
            'price'
        ]
