from django.urls import path
from .views import create_comment

app_name = "comments"

urlpatterns = [path("create/<int:pk>/", create_comment, name="create")]
