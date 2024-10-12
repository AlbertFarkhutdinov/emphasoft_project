"""Module for updating user instances that already exist,
when CustomUserProfile model is changed"""
from django.core.management.base import BaseCommand
from auth_app.models import CustomUser, CustomUserProfile


class Command(BaseCommand):
    """Class for command 'python manage.py update_db'"""
    def handle(self, *args, **options):
        """Logic of command 'python manage.py update_db'"""
        users = CustomUser.objects.all()
        for user in users:
            CustomUserProfile.objects.get(user=user).delete()
            CustomUserProfile.objects.create(user=user).save()
