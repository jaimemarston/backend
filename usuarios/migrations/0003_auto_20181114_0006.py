# Generated by Django 2.1.1 on 2018-11-14 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20181113_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='sexo',
            field=models.IntegerField(null=True),
        ),
    ]
