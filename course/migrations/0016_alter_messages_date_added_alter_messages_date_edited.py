# Generated by Django 4.1.3 on 2022-12-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_messages_date_added_messages_date_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date_edited',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
