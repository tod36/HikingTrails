# Generated by Django 5.1.3 on 2024-12-02 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trails', '0008_rename_user_comment_hiker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='hiker',
            new_name='user',
        ),
    ]
