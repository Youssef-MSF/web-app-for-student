# Generated by Django 3.1.2 on 2020-10-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forStudents', '0005_remove_comment_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nb_comments',
            field=models.IntegerField(default=0),
        ),
    ]
