# Generated by Django 5.0.7 on 2024-08-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_family_image_alter_icecream_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='image',
            field=models.ImageField(upload_to='home/images/'),
        ),
    ]
