from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(null=False)

    def __str__(self):
        return f"{self.email}"
