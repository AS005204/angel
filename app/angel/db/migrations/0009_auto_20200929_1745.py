# Generated by Django 3.0.3 on 2020-09-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20200929_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='age',
            field=models.TextField(blank=True, max_length=159, null=True),
        ),
    ]
