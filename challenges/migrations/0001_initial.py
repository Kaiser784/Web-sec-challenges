# Generated by Django 3.1.7 on 2021-03-01 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='challenges_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('venari', models.PositiveIntegerField(blank=True, default=0)),
                ('location', models.CharField(max_length=50)),
                ('difficulty', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=20)),
                ('flag', models.CharField(max_length=150)),
                ('hints', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeUserRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(blank=True, default=False)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.challenges_table', to_field='title')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.AddField(
            model_name='challenges_table',
            name='users',
            field=models.ManyToManyField(through='challenges.ChallengeUserRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
