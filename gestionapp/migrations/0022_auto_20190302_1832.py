# Generated by Django 2.1.1 on 2019-03-02 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0021_mcotizacion_opcviaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='CotizacionEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='dcotizacion',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionapp.CotizacionEstado'),
        ),
        migrations.AlterField(
            model_name='dgasto',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionapp.CotizacionEstado'),
        ),
        migrations.AlterField(
            model_name='dguia',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionapp.CotizacionEstado'),
        ),
    ]