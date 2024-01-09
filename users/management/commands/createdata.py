from django.core.management.base import BaseCommand
from faker import Faker
class Command(BaseCommand):
    help = "create fake users"

    def handle(self, *args, **kwargs):
        fake = Faker()

