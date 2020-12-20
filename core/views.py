from django.shortcuts import redirect, render
from posts.models import Post


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", {"posts": posts})
    else:
        return render(request, "home.html")
