# Generated by Django 3.0.4 on 2020-03-31 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matching', '0007_history_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='looser',
        ),
        migrations.RemoveField(
            model_name='history',
            name='winner',
        ),
        migrations.AddField(
            model_name='history',
            name='player1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='as_player1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='history',
            name='player2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='as_player2', to=settings.AUTH_USER_MODEL),
        ),
    ]
