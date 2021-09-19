from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True, verbose_name='email')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
