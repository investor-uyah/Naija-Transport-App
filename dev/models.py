from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
import datetime

# Create your models here.

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="dev_user_groups",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="dev_user_permissions",
        related_query_name="custom_user_permission",
    )
    phone_number = models.CharField(max_length=15, blank=False, null=False)

