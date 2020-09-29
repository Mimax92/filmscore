# Generated by Django 3.1.1 on 2020-09-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0027_auto_20200928_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Comedy'), (5, 'Sci-Fi'), (7, 'Drama'), (0, 'Other'), (6, 'Fantasy'), (4, 'Family'), (2, 'Action'), (3, 'Horror')], default=0),
        ),
    ]
