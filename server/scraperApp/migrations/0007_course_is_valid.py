# Generated by Django 4.1.5 on 2023-01-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0006_logo_remove_course_image_course_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]