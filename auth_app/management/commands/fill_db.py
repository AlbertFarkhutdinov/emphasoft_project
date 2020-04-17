"""Module for filling database with initial data"""
from django.core.management.base import BaseCommand
from django.conf import settings
from auth_app.models import CustomUser


class Command(BaseCommand):
    """Class for command 'python manage.py fill_db'"""
    def handle(self, *args, **options):
        """Logic of command 'python manage.py fill_db'"""
        CustomUser.objects.all().delete()
        if settings.SUPERUSER:
            CustomUser.objects.create_superuser(**settings.SUPERUSER)
