# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria')),
            ],
        ),
    ]
