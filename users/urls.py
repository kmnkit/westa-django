from django.urls import path
from django.contrib.auth import views
from .views import LoginView, LogoutView, SignUpView, ProfileUpdateView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "<int:pk>/profile-update/", ProfileUpdateView.as_view(), name="profile-update"
    ),
]
