# Generated by Django 3.0.6 on 2020-05-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20200523_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='none', upload_to='article_images/'),
        ),
    ]
