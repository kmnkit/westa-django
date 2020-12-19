from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10
    paginate_orphans = 5
    ordering = ["created_at"]
    context_object_name = "posts"
