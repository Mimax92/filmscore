# Generated by Django 3.1.1 on 2020-09-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0008_auto_20200928_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(6, 'Fantasy'), (1, 'Comedy'), (3, 'Horror'), (5, 'Sci-Fi'), (2, 'Action'), (4, 'Family'), (0, 'Other'), (7, 'Drama')], default=0),
        ),
    ]
