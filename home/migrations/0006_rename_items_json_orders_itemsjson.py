# Generated by Django 5.0.7 on 2024-08-01 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_orders_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='items_json',
            new_name='itemsJson',
        ),
    ]