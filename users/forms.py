from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_password2(self):
        return super().clean_password2()


class LoginForm(AuthenticationForm):
    # widget은 실제 렌더링할 필드.
    # nickname = forms.CharField()
    pass
