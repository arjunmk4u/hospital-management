# create_users.py

from django.core.management.base import BaseCommand
from home.utils import create_users_from_model

class Command(BaseCommand):
    help = 'Creates users from a model'

    def handle(self, *args, **options):
        message = create_users_from_model()
        self.stdout.write(self.style.SUCCESS(message))
