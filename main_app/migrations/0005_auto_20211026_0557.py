# Generated by Django 3.2.8 on 2021-10-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211025_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='unnamed.png', null=True, upload_to='profile'),
        ),
    ]