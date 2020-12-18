from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("user/", include("users.urls", namespace="users")),
    # path("post/", include("posts.urls", namespace="posts")),
    # path("favs/", include("favs.urls", namespace="favs")),
    # path("chat/", include("chats.urls", namespace="chats")),
    # path("comment/", include("comments.urls", namespace="comments")),
    path("admin/", admin.site.urls),
]
