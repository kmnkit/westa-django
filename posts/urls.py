from django.urls import path
from .views import PostListView

app_name = "posts"

urlpatterns = [
    path("list/", PostListView.as_view(), name="list"),
]
