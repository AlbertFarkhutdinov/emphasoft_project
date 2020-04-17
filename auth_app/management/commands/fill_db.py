"""Module for filling database with initial data"""
import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from auth_app.models import CustomUser


def load_from_json(file_name):
    """Function for loading data from JSON file"""
    with open(os.path.join(settings.JSON_DIR, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    """Class for command 'python manage.py fill_db'"""
    def handle(self, *args, **options):
        """Logic of command 'python manage.py fill_db'"""
        CustomUser.objects.all().delete()
        superuser = load_from_json('local_settings')['SUPERUSER']
        CustomUser.objects.create_superuser(**superuser)
