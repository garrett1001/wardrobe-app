from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='images/avatars')
   biography = models.CharField(max_length=200)
   private = models.BooleanField(default=False)