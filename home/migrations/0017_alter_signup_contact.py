# Generated by Django 5.0.7 on 2024-07-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_signup_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.IntegerField(default=False),
        ),
    ]
