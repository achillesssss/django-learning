from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('content',)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')