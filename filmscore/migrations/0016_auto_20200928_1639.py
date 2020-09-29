# Generated by Django 3.1.1 on 2020-09-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0015_auto_20200928_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Family'), (5, 'Sci-Fi'), (0, 'Other'), (3, 'Horror'), (7, 'Drama'), (2, 'Action'), (6, 'Fantasy'), (1, 'Comedy')], default=0),
        ),
    ]
