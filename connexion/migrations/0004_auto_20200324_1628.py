# Generated by Django 3.0.4 on 2020-03-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0003_forgotten_pass_reinitialized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgotten_pass',
            name='link_key',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
