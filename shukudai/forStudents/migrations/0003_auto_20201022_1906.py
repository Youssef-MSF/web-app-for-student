# Generated by Django 3.1.2 on 2020-10-22 18:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forStudents', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 18, 6, 47, 100354, tzinfo=utc)),
        ),
    ]
