# Generated by Django 4.1.3 on 2022-12-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_date_added_course_date_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]