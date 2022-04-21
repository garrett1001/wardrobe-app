from distutils import core
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')
   bio = models.TextField(blank=True)
   private = models.BooleanField(default=False)

   def __str__(self):
      return self.user.username