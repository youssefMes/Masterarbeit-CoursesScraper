# Generated by Django 4.1.4 on 2023-01-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0002_alter_percentage_title_alter_star_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percentage',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]