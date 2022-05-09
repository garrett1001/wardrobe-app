from distutils import core
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
   user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
   avatar = models.ImageField(default='default_avatar.png', upload_to='avatars')
   bio = models.TextField(max_length=500, blank=True)
   private = models.BooleanField(default=False)
   followers = models.ManyToManyField(User, blank=True, related_name='followers')

   def __str__(self):
      return self.user.username

class Message(models.Model):
   sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
   receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
   body = models.TextField(max_length=1000)
   date = models.DateTimeField(auto_now_add=True)
   is_read = models.BooleanField(default=False)