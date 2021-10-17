from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True, verbose_name='email')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'


class Blog(models.Model):
    user = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=120)
    content = models.TextField()
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:30]
