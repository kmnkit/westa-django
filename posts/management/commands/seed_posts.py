import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from posts.models import Post, Photo

NAME = "게시글"


class Command(BaseCommand):

    help = f"{NAME}을 만듭니다."

    def handle(self, *args, **options):
        users = User.objects.all()
        post_seeder = Seed.seeder()
        post_seeder.add_entity(
            Post,
            100,
            {
                "description": lambda x: post_seeder.faker.sentence(),
                "user": lambda x: random.choice(users),
            },
        )
        post_seeder.execute()

        posts = Post.objects.all()
        for post in posts:
            for i in range(random.randint(1, 3)):
                Photo.objects.create(
                    caption=post_seeder.faker.sentence(),
                    post=post,
                    photo=f"post_photos/{random.randint(1,32)}.webp",
                )
        self.stdout.write(self.style.SUCCESS(f"100개의 {NAME} Seed가 모두 만들어졌습니다."))
