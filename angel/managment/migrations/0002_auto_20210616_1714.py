# Generated by Django 3.0.3 on 2021-06-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='operator',
            new_name='description',
        ),
        migrations.AddField(
            model_name='education',
            name='timeDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='squad',
            field=models.TextField(default=1, max_length=159),
            preserve_default=False,
        ),
    ]
