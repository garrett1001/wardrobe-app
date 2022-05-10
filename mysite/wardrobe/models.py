from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Top(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/garments/tops')
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bottom(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/garments/bottoms')
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Outerwear(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/garments/outerwear')
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Footwear(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/garments/footwear')
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/garments/accessories')
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/outfits')
    description = models.TextField(max_length=300, blank=True)
    tops = models.ManyToManyField(Top, blank=True)
    bottoms = models.ManyToManyField(Bottom)
    outerwear = models.ManyToManyField(Outerwear, blank=True)
    footwear = models.ManyToManyField(Footwear)
    accessories = models.ManyToManyField(Accessory, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name