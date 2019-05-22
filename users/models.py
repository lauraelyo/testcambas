from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver


class CustomUser(AbstractUser):
    pass
    
    def __str__(self):
        return self.email
