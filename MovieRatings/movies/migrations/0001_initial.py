# Generated by Django 2.0.7 on 2018-07-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=9)),
                ('primaryTitle', models.CharField(max_length=255)),
                ('startYear', models.IntegerField(max_length=4)),
                ('runtimeMinutes', models.IntegerField(max_length=5)),
                ('genres', models.CharField(max_length=32)),
            ],
        ),
    ]
