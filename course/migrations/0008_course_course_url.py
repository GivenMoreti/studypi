# Generated by Django 4.1.3 on 2022-12-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_student_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_url',
            field=models.CharField(max_length=8000, null=True),
        ),
    ]
