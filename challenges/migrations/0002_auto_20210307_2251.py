# Generated by Django 3.1.7 on 2021-03-07 17:21

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField('challenges_table', 'location', models.URLField(max_length=50)),
        migrations.AddField(
            model_name='challenges_table',
            name = 'author_link',
            field=models.URLField(max_length=50, blank=True, default=''),
        ),
    ]
