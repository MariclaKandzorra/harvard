# Generated by Django 4.0.3 on 2022-03-21 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_task_completed_date_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 5, 20, 52, 14, 966453), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 5, 20, 52, 14, 966293), null=True),
        ),
    ]
