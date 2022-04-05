# Generated by Django 4.0.3 on 2022-03-26 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='filename',
            new_name='file_name',
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 10, 19, 57, 26, 557375), null=True),
        ),
    ]
