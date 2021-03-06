# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-27 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('startpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=45)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adder', to='startpage.User')),
                ('others', models.ManyToManyField(related_name='also_wants', to='startpage.User')),
            ],
        ),
    ]
