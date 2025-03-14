from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(null= True, blank=True, max_length=200)

    def __str__(self):
        return self.username

