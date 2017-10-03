# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('py_proj_man', '0003_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='baseline',
        ),
        migrations.AlterField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='py_proj_man.Task'),
        ),
    ]
