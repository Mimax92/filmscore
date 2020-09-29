# Generated by Django 3.1.1 on 2020-09-28 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0006_auto_20200924_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genres',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Sci-Fi'), (1, 'Comedy'), (7, 'Drama'), (0, 'Other'), (2, 'Action'), (3, 'Horror'), (6, 'Fantasy'), (4, 'Family')], default=0),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(blank=True, default='', max_length=1000)),
                ('stars', models.PositiveSmallIntegerField(default=3)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmscore.film')),
            ],
        ),
    ]
