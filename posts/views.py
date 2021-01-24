from posts.forms import CreatePostForm
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from comments.forms import CreateCommentForm


class PostListView(ListView):
    model = Post
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "posts"
    template_name = "posts/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateCommentForm()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateCommentForm()
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ["photo", "description"]
    template_name = "posts/post_create.html"

    def post(self, request, *args, **kwargs):
        new_post = super().post(request, *args, **kwargs)
        new_post.user = request.user
        return new_post
