# Generated by Django 3.0.6 on 2020-05-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200521_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_path',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='none', upload_to='articles/'),
        ),
    ]
