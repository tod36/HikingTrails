# Generated by Django 5.1.3 on 2024-12-02 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trails', '0007_alter_trails_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='hiker',
        ),
    ]
