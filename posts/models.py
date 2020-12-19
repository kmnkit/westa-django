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

    def upload_path(self, filename):
        if not self.pk:
            instance = Post.objects.create()
            self.id = self.pk = instance.id
        return f"post_photos/{self.id}"

    photo = models.ImageField(null=True, blank=True, upload_to=upload_path)
