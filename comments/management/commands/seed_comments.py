import random
from django.core.management.base import BaseCommand
from comments.models import Comment
from posts.models import Post
from users.models import User
from django_seed import Seed

NAME = "댓글"


class Command(BaseCommand):

    help = f"{NAME} 더미 데이터를 생성"

    def add_arguments(self, parser):
        parser.add_argument("--total", help="코멘트를 몇 개 만들 건가요?", default=10)

    def handle(self, *args, **options):
        posts = Post.objects.all()
        users = User.objects.all()
        faker = Seed.faker()

        total = int(options.get("total"))
        seeder = Seed.seeder()
        seeder.add_entity(
            Comment,
            total,
            {
                "post": lambda x: random.choice(posts),
                "user": lambda x: random.choice(users),
                "text": lambda x: faker.sentence(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total}개의 {NAME} 더미 데이터 생성!"))
