# Generated by Django 2.0.8 on 2019-02-28 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0016_auto_20190227_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcotizacion',
            name='horafin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dcotizacion',
            name='horaini',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dgasto',
            name='horafin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dgasto',
            name='horaini',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dguia',
            name='horafin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dguia',
            name='horaini',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mcotizacion',
            name='horafin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mcotizacion',
            name='horaini',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
