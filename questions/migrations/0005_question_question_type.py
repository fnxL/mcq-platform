# Generated by Django 3.2.5 on 2021-07-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_alter_question_negative_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.IntegerField(default=0),
        ),
    ]