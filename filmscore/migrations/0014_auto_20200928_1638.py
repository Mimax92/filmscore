# Generated by Django 3.1.1 on 2020-09-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0013_auto_20200928_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Action'), (6, 'Fantasy'), (5, 'Sci-Fi'), (1, 'Comedy'), (7, 'Drama'), (4, 'Family'), (3, 'Horror'), (0, 'Other')], default=0),
        ),
    ]
