from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "password1", "password2")
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"


class DeleteUser(ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        name = forms.CharField()
