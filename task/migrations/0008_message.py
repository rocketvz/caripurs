# Generated by Django 2.1.7 on 2020-09-19 16:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_task_task_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_pressure_in', models.CharField(blank=True, max_length=255)),
                ('sensor_pressure_out', models.CharField(blank=True, max_length=255)),
                ('sensor_toc', models.CharField(blank=True, max_length=255)),
                ('sensor_cod', models.CharField(blank=True, max_length=255)),
                ('sensor_uv254', models.CharField(blank=True, max_length=255)),
                ('sensor_air_pressure', models.CharField(blank=True, max_length=255)),
                ('sensor_temperature', models.CharField(blank=True, max_length=255)),
                ('sensor_altitude', models.CharField(blank=True, max_length=255)),
                ('sensor_cistern', models.CharField(blank=True, max_length=255)),
                ('sensor_flow', models.CharField(blank=True, max_length=255)),
                ('sensor_asu_p10', models.CharField(blank=True, max_length=255)),
                ('sensor_asu_p25', models.CharField(blank=True, max_length=255)),
                ('sensor_asu_p100', models.CharField(blank=True, max_length=255)),
                ('sensor_aeu_p10', models.CharField(blank=True, max_length=255)),
                ('sensor_aeu_p25', models.CharField(blank=True, max_length=255)),
                ('sensor_aeu_p100', models.CharField(blank=True, max_length=255)),
                ('sensor_practice03', models.CharField(blank=True, max_length=255)),
                ('sensor_practice05', models.CharField(blank=True, max_length=255)),
                ('sensor_practice10', models.CharField(blank=True, max_length=255)),
                ('sensor_practice25', models.CharField(blank=True, max_length=255)),
                ('sensor_practice50', models.CharField(blank=True, max_length=255)),
                ('sensor_practice100', models.CharField(blank=True, max_length=255)),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
