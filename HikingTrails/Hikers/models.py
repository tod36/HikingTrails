from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.db import models


# class Hiker(AbstractUser, PermissionsMixin):
#     age = models.IntegerField(null=True, blank=True)
#     phone = models.CharField(max_length=15, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
#     hiker_image = models.ImageField(upload_to='hiker_images/', null=True, blank=True)
#     is_approved = models.BooleanField(default=False)
#
#     groups = models.ManyToManyField(
#         Group,
#         related_name='hiker_set',  # Change this to your desired related_name
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='hiker_permissions_set',  # Change this to your desired related_name
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )


class Hiker(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    hiker_image = models.ImageField(upload_to='hiker_images/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='hiker_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='hiker_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
