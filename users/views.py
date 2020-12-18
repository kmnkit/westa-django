from users.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, SignUpForm


class SignUpView(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForm


class LoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm

    def form_invalid(self, form):
        messages.error(self.request, "로그인에 실패하였습니다.")
        return super().form_invalid(form)


class LogoutView(LogoutView):
    pass


class ProfileView(DetailView):
    model = User
    template_name = "users/profile.html"


class ProfileUpdateView(UpdateView):
    model = User
    template_name = "users/update-profile.html"
