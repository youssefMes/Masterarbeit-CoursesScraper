# Generated by Django 4.1.5 on 2023-01-05 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraperApp', '0005_remove_course_image_url_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('image', models.ImageField(max_length=500, null=True, upload_to='./static/')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='logo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scraperApp.logo'),
        ),
    ]
