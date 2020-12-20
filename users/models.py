from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):

    email = models.EmailField(verbose_name="이메일 주소", max_length=255, unique=True)
    birthday = models.DateField("생일", blank=True, null=True)
    is_active = models.BooleanField("활성화된 계정", default=True)
    is_admin = models.BooleanField("운영자 계정", default=False)
    nickname = models.CharField(verbose_name="닉네임", max_length=16, unique=True)

    REQUIRED_FIELDS = ["email", "nickname"]

    def __str__(self):
        return self.email

    def get_posts_count(self):
        return self.posts.count()

    get_posts_count.short_description = "게시물 수"

    def upload_path(self, filename):
        if not self.pk:
            instance = User.objects.create()
            self.id = self.pk = instance.id
        return f"user_avatar/{self.id}/{filename}"

    avatar = models.ImageField(upload_to=upload_path, blank=True)

    def get_absolute_url(self):
        return reverse("users:user", kwargs={"pk": self.pk})

    def get_avatar(self):
        try:
            return self.avatar.url
        except ValueError:
            return "/media/user_avatar/anonymous.jpeg"

    def get_following_count(self):
        return self.following_list.count()

    get_following_count.short_description = "팔로잉 수"

    def get_followed_count(self):
        return self.followed_list.count()

    get_followed_count.short_description = "팔로워 수"