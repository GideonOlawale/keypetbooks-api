# Generated by Django 3.1.7 on 2021-03-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=50)),
                ('csv_continents', models.CharField(max_length=50)),
                ('locations', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('total_cases', models.IntegerField()),
                ('new_cases', models.IntegerField()),
                ('total_cases_per_million', models.FloatField()),
                ('new_cases_per_million', models.FloatField()),
                ('new_cases_smoothed_per_million', models.FloatField()),
                ('total_deaths_per_million', models.FloatField()),
                ('new_deaths_per_million', models.FloatField()),
                ('new_deaths_smoothed_per_million', models.FloatField()),
            ],
        ),
    ]
