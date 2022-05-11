# Generated by Django 4.0.2 on 2022-05-11 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0003_alter_outfit_tops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='image',
            field=models.ImageField(upload_to='uploads/garments/accessories'),
        ),
        migrations.AlterField(
            model_name='bottom',
            name='image',
            field=models.ImageField(upload_to='uploads/garments/bottoms'),
        ),
        migrations.AlterField(
            model_name='footwear',
            name='image',
            field=models.ImageField(upload_to='uploads/garments/footwear'),
        ),
        migrations.AlterField(
            model_name='outerwear',
            name='image',
            field=models.ImageField(upload_to='uploads/garments/outerwear'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='bottoms',
            field=models.ManyToManyField(blank=True, to='wardrobe.Bottom'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='footwear',
            field=models.ManyToManyField(blank=True, to='wardrobe.Footwear'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='image',
            field=models.ImageField(upload_to='uploads/outfits'),
        ),
        migrations.AlterField(
            model_name='top',
            name='image',
            field=models.ImageField(upload_to='uploads/garments/tops'),
        ),
    ]