from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        max_length=127,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(
        null=True,
        default=None,
        blank=True,
    )
    is_employee = models.BooleanField(default=False)
