from django.contrib import admin

from .models import Outfit, Top, Bottom, Outerwear, Footwear, Accessory

# Register your models here.
# admin.site.register(Garment)
admin.site.register(Outfit)
admin.site.register(Top)
admin.site.register(Bottom)
admin.site.register(Outerwear)
admin.site.register(Footwear)
admin.site.register(Accessory)