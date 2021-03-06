# Generated by Django 3.0 on 2020-12-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20201214_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='position',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.Topic'),
            preserve_default=False,
        ),
    ]
