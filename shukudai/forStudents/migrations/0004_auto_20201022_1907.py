# Generated by Django 3.1.2 on 2020-10-22 18:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forStudents', '0003_auto_20201022_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
