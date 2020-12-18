from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(verbose_name="이메일 주소", max_length=255, unique=True)
    birthday = models.DateField(u"생일", blank=True, null=True)
    is_active = models.BooleanField(u"활성화된 계정", default=True)
    is_admin = models.BooleanField(u"운영자 계정", default=False)
    nickname = models.CharField(verbose_name="ID", max_length=16, unique=True)
    REQUIRED_FIELDS = ["email", "nickname"]

    def __str__(self):
        return self.email

    def posts_count(self):
        return self.posts.count()

    posts_count.short_description = "게시물 수"
