# Generated by Django 5.1.1 on 2025-02-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_alter_courseschedule_recurrence_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseschedule',
            name='recurrence_rule',
            field=models.TextField(blank=True, null=True),
        ),
    ]
