# Generated by Django 3.0.4 on 2020-04-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0012_finale_poule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finale_poule',
            name='level',
            field=models.CharField(default='', max_length=20),
        ),
    ]