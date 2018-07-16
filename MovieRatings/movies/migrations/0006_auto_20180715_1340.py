# Generated by Django 2.0.7 on 2018-07-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20180713_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actor_1_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor_2_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor_3_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='aspect_ratio',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='cast_total_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='color',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='facenumber_in_poster',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_facebook_likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='num_critic_for_reviews',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='plot_keywords',
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='gross',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='num_user_for_reviews',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_year',
            field=models.IntegerField(),
        ),
    ]
