# Generated by Django 2.1.1 on 2019-06-23 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20190621_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert', models.CharField(blank=True, max_length=50, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('starttask', models.DateTimeField(blank=True, null=True)),
                ('endtask', models.DateTimeField(blank=True, null=True)),
                ('start_longitude', models.FloatField(blank=True, null=True)),
                ('end_longitude', models.FloatField(blank=True, null=True)),
                ('start_latitude', models.FloatField(blank=True, null=True)),
                ('end_latitude', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuarios')),
            ],
        ),
        migrations.DeleteModel(
            name='Usertraking',
        ),
    ]