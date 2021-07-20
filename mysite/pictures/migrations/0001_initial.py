# Generated by Django 3.2.5 on 2021-07-20 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('dateTaken', models.DateField(default=datetime.datetime.now, verbose_name='The date and time the photo was taken')),
                ('takenBy', models.CharField(max_length=100, verbose_name='The person which has taken the photo')),
            ],
        ),
    ]
