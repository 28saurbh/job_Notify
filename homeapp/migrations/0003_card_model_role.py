# Generated by Django 3.1.7 on 2022-02-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_auto_20220210_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_model',
            name='role',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
