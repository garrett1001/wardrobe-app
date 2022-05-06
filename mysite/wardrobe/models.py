from unicodedata import category
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = [
    ('Tops', 'Tops'),
    ('Bottoms', 'Bottoms'),
    ('Outerwear', 'Outerwear'),
    ('Footwear', 'Footwear'),
    ('Accessories', 'Accessories'),
]

class Garment(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='garments')
    description = models.TextField(max_length=300, blank=True)
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='outfits')
    description = models.TextField(max_length=300, blank=True)
    garments = models.ManyToManyField(Garment)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name