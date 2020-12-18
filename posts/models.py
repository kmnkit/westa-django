from django.db import models
from core.models import TimeStampedModel


class Post(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.CASCADE
    )
    description = models.TextField(max_length=500, blank=True)
    fav_users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return self.description


class Photo(TimeStampedModel):
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField()
    caption = models.TextField()

    def __str__(self):
        return self.caption
