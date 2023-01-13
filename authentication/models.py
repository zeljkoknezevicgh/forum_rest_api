from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.managers import CustomUserManager



class User(AbstractUser):

    REQUIRED_FIELDS = ['password', 'email']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"



