# Generated by Django 4.1.4 on 2022-12-24 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0004_bookmark'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('user', 'course')},
        ),
    ]
