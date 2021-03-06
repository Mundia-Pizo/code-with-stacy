# Generated by Django 3.0 on 2020-12-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20201214_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='new_sli'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(upload_to='topics'),
        ),
    ]
