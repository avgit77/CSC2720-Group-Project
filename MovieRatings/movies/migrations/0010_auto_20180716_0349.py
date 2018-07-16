# Generated by Django 2.0.7 on 2018-07-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20180716_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userratings',
            name='movie',
        ),
        migrations.AddField(
            model_name='userratings',
            name='movie_title',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userratings',
            name='title_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]