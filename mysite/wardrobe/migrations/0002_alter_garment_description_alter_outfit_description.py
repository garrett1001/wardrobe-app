# Generated by Django 4.0.2 on 2022-05-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garment',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
