# Generated by Django 4.1.3 on 2022-12-03 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_student_image_file_alter_course_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image_file',
        ),
    ]