# Generated by Django 5.0.7 on 2024-07-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_signup_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.IntegerField(null=True),
        ),
    ]
