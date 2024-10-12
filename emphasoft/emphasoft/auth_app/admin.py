"""Representation of models from auth_app in the admin interface"""
from django.contrib import admin
from auth_app.models import CustomUser

admin.site.register(CustomUser)
