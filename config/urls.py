import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("user/", include("users.urls", namespace="users")),
    path("post/", include("posts.urls", namespace="posts")),
    path("follower/", include("followers.urls", namespace="followers")),
    path("favs/", include("favs.urls", namespace="favs")),
    # path("chat/", include("chats.urls", namespace="chats")),
    path("comment/", include("comments.urls", namespace="comments")),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)