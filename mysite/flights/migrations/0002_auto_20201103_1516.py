# Generated by Django 2.2.12 on 2020-11-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
