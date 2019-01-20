# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-20 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kratos', '0003_ambassadorinfo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('task_type', models.CharField(choices=[('manual', 'Manual'), ('monitored', 'Monitored')], default='student', max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='ambassadorinfo',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ambassadorinfo',
            name='professional_status',
            field=models.CharField(choices=[('student', 'Student'), ('looking', 'Looking For Job'), ('employed', 'Employed')], default='student', max_length=100),
        ),
        migrations.AlterField(
            model_name='ambassadorinfo',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('on_hold', 'On Hold'), ('selected', 'Selected')], default='applied', max_length=100),
        ),
    ]
