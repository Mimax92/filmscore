# Generated by Django 3.1.1 on 2020-09-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0019_auto_20200928_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Other'), (2, 'Action'), (5, 'Sci-Fi'), (3, 'Horror'), (1, 'Comedy'), (7, 'Drama'), (4, 'Family'), (6, 'Fantasy')], default=0),
        ),
    ]
