# Generated by Django 3.0 on 2020-12-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20201120_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='new.png', upload_to='articles'),
            preserve_default=False,
        ),
    ]
