# Generated by Django 5.1.1 on 2025-02-25 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0002_initial'),
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseschedule',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='professors.professor'),
        ),
    ]
