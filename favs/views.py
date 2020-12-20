from django.shortcuts import redirect, reverse
from django.views.generic import ListView
from .models import FavList
from posts.models import Post


class FavListView(ListView):
    model = FavList
    template_name = "favs/fav_list.html"
    context_object_name = "favs"


def toggle_fav(request, pk):
    user = request.user

    if user.is_authenticated:
        posts = Post.objects.all()
        post = posts.get(pk=pk)
        if post is not None:
            print(FavList.objects.get_or_create(user=user))
            fav_list, _ = FavList.objects.get_or_create(user=user)
            if post in fav_list.posts.all():
                fav_list.posts.remove(post)
                post.favs.remove(user)
            else:
                fav_list.posts.add(post)
                post.favs.add(user)
            fav_list.save()

            return redirect(reverse("favs:fav-list"))
