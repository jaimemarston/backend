# Generated by Django 2.0.8 on 2019-06-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20190620_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usertraking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('alert', models.CharField(blank=True, max_length=50, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('starttask', models.DateTimeField(blank=True, null=True)),
                ('endtask', models.DateTimeField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
