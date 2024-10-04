# Generated by Django 5.0.7 on 2024-10-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_suggestion_suggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='email',
            field=models.CharField(default=False, max_length=122),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestions',
            field=models.TextField(max_length=800, null=True),
        ),
    ]
