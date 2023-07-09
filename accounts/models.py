from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30,unique=True)
    user_bio = models.TextField(max_length=103)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to="user/")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    facebook_username = models.CharField(max_length=50, blank=True)
    instagram_username = models.CharField(max_length=50, blank=True)
    linkedin_username = models.CharField(max_length=50, blank=True)
    github_username = models.CharField(max_length=50, blank=True)
    youtube_username = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.user} social links"
    
