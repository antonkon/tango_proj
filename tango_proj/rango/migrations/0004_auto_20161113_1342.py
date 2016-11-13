# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20161113_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='view',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=128, verbose_name='стр'),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
