# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('autoplay', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='active_images',
            field=models.ManyToManyField(blank=True, to='app.Image'),
        ),
    ]