# Generated by Django 4.2.1 on 2023-06-03 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_picture_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='date_picture',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]