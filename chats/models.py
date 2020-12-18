from django.db import models
from core.models import TimeStampedModel


class Chat(TimeStampedModel):
    user = models.ManyToManyField("users.User")


class Message(TimeStampedModel):
    chat = models.ForeignKey("Chat", related_name="messages", on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE, blank=True
    )
