from users.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginForm, SignUpForm
from . import mixins


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
    context_object_name = "user_obj"


class ProfileUpdateView(UpdateView):
    model = User
    template_name = "users/update-profile.html"

    fields = ("email", "nickname")

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(
    mixins.LoggedInOnlyView,
    SuccessMessageMixin,
    PasswordChangeView,
):

    template_name = "users/update-password.html"
    success_message = "비밀번호가 변경되었습니다."

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["old_password"].widget.attrs = {"placeholder": "Current Password"}
        form.fields["new_password1"].widget.attrs = {"placeholder": "New Password"}
        form.fields["new_password2"].widget.attrs = {
            "placeholder": "Confirm New Password"
        }
        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()
