# Generated by Django 3.1.5 on 2021-02-02 13:47

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
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=300)),
                ('goal_id', models.IntegerField()),
                ('created_by', models.CharField(max_length=300)),
                ('moved_by', models.CharField(max_length=300)),
                ('owner', models.CharField(max_length=300)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='moshoodscrumy.goalstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_to_scrumy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_by', models.CharField(max_length=300)),
                ('created_by', models.CharField(max_length=300)),
                ('moved_from', models.CharField(max_length=300)),
                ('moved_to', models.CharField(max_length=300)),
                ('time_of_action', models.DateTimeField(auto_now_add=True, null=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='moshoodscrumy.scrumygoals')),
            ],
        ),
    ]
