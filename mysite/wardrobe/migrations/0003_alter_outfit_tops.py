# Generated by Django 4.0.2 on 2022-05-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0002_alter_outfit_accessories_alter_outfit_outerwear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='tops',
            field=models.ManyToManyField(blank=True, to='wardrobe.Top'),
        ),
    ]
