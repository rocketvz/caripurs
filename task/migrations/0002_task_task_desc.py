# Generated by Django 2.1.7 on 2019-02-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_desc',
            field=models.TextField(blank=True),
        ),
    ]
