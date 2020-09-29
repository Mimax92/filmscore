# Generated by Django 3.1.1 on 2020-09-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0005_auto_20200924_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Comedy'), (4, 'Family'), (2, 'Action'), (6, 'Fantasy'), (3, 'Horror'), (5, 'Sci-Fi'), (7, 'Drama'), (0, 'Other')], default=0),
        ),
    ]
