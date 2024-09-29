from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500'
        })
    )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password',
            'class': 'w-full p-2 border border-gray-300 rounded-lg focus:ring-teal-500 focus:border-teal-500'
        })
    )