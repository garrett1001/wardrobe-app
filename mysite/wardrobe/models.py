from unicodedata import category
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
    ('Top', 'Top'),
    ('Bottom', 'Bottom'),
    ('Outerwear', 'Outerwear'),
    ('Footwear', 'Footwear'),
    ('Accessory', 'Accessory'),
]

class Garment(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='garments')
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=9, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='outfits')
    description = models.CharField(max_length=200)
    garments = models.ManyToManyField(Garment)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name