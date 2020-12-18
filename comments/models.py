from django.db import models
from django.db.models.fields import related
from core.models import TimeStampedModel


class Comment(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "posts.Post", related_name="comments", on_delete=models.CASCADE
    )
    text = models.TextField()
