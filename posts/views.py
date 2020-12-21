from django.views.generic import ListView
from .models import Post
from comments.forms import CreateCommentForm


class PostListView(ListView):
    model = Post
    paginate_by = 10
    paginate_orphans = 5
    ordering = ["-created_at"]
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["form"] = CreateCommentForm()
        return context
