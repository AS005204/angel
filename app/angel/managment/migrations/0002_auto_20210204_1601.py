# Generated by Django 3.0.3 on 2021-02-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='education',
            field=models.ManyToManyField(blank=True, to='managment.Education'),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='searchSquad',
            field=models.ManyToManyField(blank=True, to='managment.SearchSquad'),
        ),
    ]
