# Generated by Django 2.0.8 on 2019-09-03 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0042_chofer_brevete'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidad',
            name='empglp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unidad',
            name='emprevtec',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unidad',
            name='empsegveh',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unidad',
            name='empsoat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
