from django.shortcuts import redirect, reverse
from .forms import CreateCommentForm
from posts.models import Post
from django.urls import reverse_lazy


def create_comment(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateCommentForm(request.POST)
            post = Post.objects.get(pk=pk)
            if not post:
                return redirect(reverse("core:home"))
            if form.is_valid():
                comment = form.save()
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect(reverse("core:home"))
    else:
        return redirect(reverse_lazy("users:login"))
