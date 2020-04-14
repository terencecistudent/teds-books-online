# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_auto_20200406_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=50)),
                ('street_address2', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.UserOrder'),
        ),
    ]