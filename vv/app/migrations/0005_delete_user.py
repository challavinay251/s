# Generated by Django 4.1.3 on 2023-05-25 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]