__author__ = 'Хедин'
from django import forms
from django.contrib.auth.forms import UserCreationForm

class regform(UserCreationForm):
    login=forms.CharField(max_length=30, min_length=6, widget=forms.TextInput(attrs={'class' :'form-control' }))
    password1=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class' :'form-control' }), min_length=6)
    password2=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class' :'form-control' }), min_length=6)
    email=forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'class' :'form-control' }))

