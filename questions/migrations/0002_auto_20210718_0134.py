# Generated by Django 3.2.5 on 2021-07-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='negative_marks',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.TextField(blank=True),
        ),
    ]
