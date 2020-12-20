from django.urls import path
from .views import toggle_follow

app_name = "followers"

urlpatterns = [path("toggle/<int:pk>/", toggle_follow, name="toggle")]
