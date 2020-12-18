from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="How many users do you want to create ",
        )

    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(User, total, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{total} users created!"))
