# Generated by Django 5.0.7 on 2024-07-16 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='signup',
        ),
    ]
