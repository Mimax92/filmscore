# Generated by Django 3.1.1 on 2020-09-24 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmscore', '0003_auto_20200911_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runtime', models.PositiveSmallIntegerField(default=0)),
                ('genres', models.PositiveSmallIntegerField(choices=[(4, 'Family'), (2, 'Action'), (6, 'Fantasy'), (5, 'Sci-Fi'), (7, 'Drama'), (3, 'Horror'), (1, 'Comedy'), (0, 'Other')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='extra_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmscore.extrainfo'),
        ),
    ]