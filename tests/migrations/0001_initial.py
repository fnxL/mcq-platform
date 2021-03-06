# Generated by Django 3.2.5 on 2021-07-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('test_type', models.IntegerField()),
                ('number_of_question', models.IntegerField(default=0)),
                ('time_limit', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('max_marks', models.IntegerField(default=0)),
            ],
        ),
    ]
