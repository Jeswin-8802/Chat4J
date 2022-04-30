from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    has_logged_in = models.BooleanField(default = False)
    image = models.ImageField(help_text='User Profile Pic', blank=True, upload_to='profile_pic')
    bio = models.TextField(help_text='User Bio', null = True)