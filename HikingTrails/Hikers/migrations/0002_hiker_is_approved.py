# Generated by Django 5.1.3 on 2024-11-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hikers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiker',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
