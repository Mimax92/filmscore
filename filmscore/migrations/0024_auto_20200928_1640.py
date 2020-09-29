# Generated by Django 3.1.1 on 2020-09-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0023_auto_20200928_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(6, 'Fantasy'), (1, 'Comedy'), (0, 'Other'), (2, 'Action'), (4, 'Family'), (7, 'Drama'), (5, 'Sci-Fi'), (3, 'Horror')], default=0),
        ),
    ]
