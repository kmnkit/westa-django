from django.db import models
from core.models import TimeStampedModel


class FollowerList(TimeStampedModel):
    """
    유저가 팔로우 한 사람의 리스트 모델
    """

    user = models.ForeignKey(
        "users.User", related_name="following_users", on_delete=models.CASCADE
    )
    following_list = models.ManyToManyField(
        "users.User", related_name="following_list", blank=True
    )

    def following_list_count(self):
        return self.following_list.count()

    following_list_count.short_description = "팔로우"

    def __str__(self):
        return f"{self.user.nickname}의 팔로우 리스트"


class FollowedList(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="followed_users", on_delete=models.CASCADE
    )
    followed_list = models.ManyToManyField(
        "users.User", related_name="followed_list", blank=True
    )

    def followed_list_count(self):
        return self.followed_list.count()

    followed_list_count.short_description = "팔로워"

    def __str__(self):
        return f"{self.user.nickname}을 팔로우 한 리스트"
