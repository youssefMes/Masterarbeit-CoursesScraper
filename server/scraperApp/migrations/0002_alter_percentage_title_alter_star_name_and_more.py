# Generated by Django 4.1.4 on 2023-01-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percentage',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='star',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='star',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]