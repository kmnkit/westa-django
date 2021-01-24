from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView

app_name = "posts"

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post"),
    path("list/", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
]
