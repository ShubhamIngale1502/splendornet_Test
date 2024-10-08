# Generated by Django 5.0.7 on 2024-08-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0006_alter_movie_review_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_review',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='reviewapp.genre'),
        ),
    ]
