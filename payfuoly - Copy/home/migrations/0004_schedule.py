# Generated by Django 5.0.2 on 2024-03-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userprofile_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('sport', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('teams', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
    ]
