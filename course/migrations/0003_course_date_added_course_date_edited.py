# Generated by Django 4.1.3 on 2022-12-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_student_date_added_student_date_edited_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='date_edited',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]