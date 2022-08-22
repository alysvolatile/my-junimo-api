# Generated by Django 4.1 on 2022-08-22 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JunimoDatabaseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('recipe_description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=150)),
                ('processor_needed', models.CharField(max_length=50)),
                ('link_to_wiki', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=150)),
                ('sale_price', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2147483647), django.core.validators.MinValueValidator(1)])),
                ('link_to_wiki', models.CharField(max_length=150)),
            ],
        ),
    ]
