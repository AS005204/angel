# Generated by Django 3.0.3 on 2021-02-08 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0002_auto_20210204_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='equipment_hisrory',
            name='crew',
        ),
        migrations.RemoveField(
            model_name='equipment_hisrory',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='crew',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='education',
        ),
        migrations.RemoveField(
            model_name='volunteers',
            name='searchSquad',
        ),
        migrations.DeleteModel(
            name='Crew',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='Equipment_hisrory',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='SearchSquad',
        ),
        migrations.DeleteModel(
            name='Volunteers',
        ),
    ]
