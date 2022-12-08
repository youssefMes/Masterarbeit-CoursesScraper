# Generated by Django 4.1.4 on 2022-12-08 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('evaluation_count', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('city', models.CharField(max_length=100)),
                ('study_start', models.CharField(max_length=100, null=True)),
                ('study_form', models.CharField(max_length=100, null=True)),
                ('study_periode', models.CharField(max_length=100, null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('languages', models.CharField(max_length=100, null=True)),
                ('website_link', models.CharField(max_length=100, null=True)),
                ('credit_points', models.CharField(max_length=50, null=True)),
                ('costs', models.CharField(max_length=100, null=True)),
                ('contents', models.TextField(null=True)),
                ('requirements', models.TextField(null=True)),
                ('models', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('report_count', models.IntegerField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraperApp.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Percentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraperApp.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('portal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraperApp.portal')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='information',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scraperApp.information'),
        ),
        migrations.AddField(
            model_name='course',
            name='portal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraperApp.portal'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('star_rating', models.CharField(max_length=5)),
                ('additional_evaluation', models.JSONField(null=True)),
                ('date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraperApp.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
