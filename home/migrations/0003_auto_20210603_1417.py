# Generated by Django 3.2.3 on 2021-06-03 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_communication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='communication',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='emailid',
            new_name='email',
        ),
    ]
