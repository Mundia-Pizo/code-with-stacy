# Generated by Django 3.0 on 2021-12-24 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
    ]