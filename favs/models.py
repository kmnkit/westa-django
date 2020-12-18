from django.db import models
from core.models import TimeStampedModel


class FavList(TimeStampedModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    post = models.ManyToManyField("posts.Post", related_name="fav_lists")

    def __str__(self):
        return f"{self.user.username}의 즐겨찾기 리스트"
