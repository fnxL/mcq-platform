# Generated by Django 3.2.5 on 2021-07-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='time_limit',
            field=models.IntegerField(blank=True),
        ),
    ]
