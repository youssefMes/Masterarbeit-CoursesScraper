# Generated by Django 4.1.5 on 2023-01-08 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0009_course_invalidated_by_alter_course_validated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scraperApp.logo'),
        ),
    ]
