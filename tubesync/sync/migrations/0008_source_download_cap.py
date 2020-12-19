# Generated by Django 3.1.4 on 2020-12-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0007_auto_20201219_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='download_cap',
            field=models.IntegerField(choices=[(0, 'No cap'), (604800, '1 week (7 days)'), (2592000, '1 month (30 days)'), (7776000, '3 months (90 days)'), (15552000, '6 months (180 days)'), (31536000, '1 year (365 days)'), (63072000, '2 years (730 days)'), (94608000, '3 years (1095 days)'), (157680000, '5 years (1825 days)'), (315360000, '10 years (3650 days)')], default=0, help_text='Do not download media older than this capped date', verbose_name='download cap'),
        ),
    ]
