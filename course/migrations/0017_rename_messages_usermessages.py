# Generated by Django 4.1.3 on 2022-12-04 08:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0016_alter_messages_date_added_alter_messages_date_edited'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='UserMessages',
        ),
    ]