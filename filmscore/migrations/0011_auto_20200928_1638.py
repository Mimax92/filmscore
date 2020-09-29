# Generated by Django 3.1.1 on 2020-09-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0010_auto_20200928_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Family'), (5, 'Sci-Fi'), (7, 'Drama'), (6, 'Fantasy'), (0, 'Other'), (3, 'Horror'), (1, 'Comedy'), (2, 'Action')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.TextField(blank=True, default=''),
        ),
    ]
