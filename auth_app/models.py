"""Models for auth_app."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    """Class for user model."""

    class Meta:
        """Correct representation of model in the admin interface."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)

    def __repr__(self):
        """String representation of model."""
        return self.username

    def __str__(self):
        """String representation of model."""
        return f'{self.first_name} {self.last_name}'


class CustomUserProfile(models.Model):
    """Class for user model profile."""

    objects = models.Manager()
    user = models.OneToOneField(
        CustomUser,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE,
    )
    friends = models.TextField(verbose_name='Friends list', blank=True)

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, *args, **kwargs):
        """Function for user profile creation."""
        if created:
            CustomUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, *args, **kwargs):
        """Function for user profile saving."""
        instance.customuserprofile.save()
