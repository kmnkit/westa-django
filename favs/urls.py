from django.urls import path
from .views import toggle_fav, FavListView

app_name = "favs"


urlpatterns = [
    path("<int:pk>/toggle-fav/", toggle_fav, name="toggle"),
    path("favs/", FavListView.as_view(), name="favs"),
]
