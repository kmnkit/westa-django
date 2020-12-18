from random import choices
from django.core.management.base import BaseCommand
from favs.models import FavList
from users.models import User
from posts.models import Post

NAME = "즐겨찾기"


class Command(BaseCommand):

    help = f"{NAME}의 더미데이터 생성"

    def handle(self, *args, **options):
        users = User.objects.all()
        posts = Post.objects.all()
        for user in users:
            fav_list = FavList.objects.create(
                user=user,
            )
            fav_list.post.set(choices(posts, k=10))
        self.stdout.write(self.style.SUCCESS(f"{NAME} created!"))
