# Generated by Django 4.1 on 2022-08-22 14:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('recipe_description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=150)),
                ('processor_needed', models.CharField(max_length=50)),
                ('link_to_wiki', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('Platform', models.CharField(max_length=30)),
                ('farm_name', models.CharField(max_length=12)),
                ('pet_type', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog')], max_length=3)),
                ('pet_name', models.CharField(max_length=12)),
                ('pet_image', models.CharField(choices=[('C1', 'Cat 1'), ('C2', 'Cat 2'), ('C3', 'Cat 2'), ('D1', 'Dog 1'), ('D2', 'Dog 2'), ('D3', 'Dog 3')], max_length=2)),
                ('love_interest', models.CharField(choices=[('AL', 'Alex'), ('EL', 'Elliot'), ('HA', 'Harvey'), ('SA', 'Sam'), ('SE', 'Sebastian'), ('SH', 'Shane'), ('AB', 'Abigail'), ('EM', 'Emily'), ('HL', 'Haley'), ('LE', 'Leah'), ('MA', 'Maru'), ('PE', 'Penny'), ('KR', 'Krobus')], max_length=2)),
                ('horse_name', models.CharField(max_length=12)),
                ('total_g', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2147483647), django.core.validators.MinValueValidator(1)])),
                ('year', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(2147483647), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=150)),
                ('sale_price', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2147483647), django.core.validators.MinValueValidator(1)])),
                ('link_to_wiki', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_needed', models.IntegerField()),
                ('blueprint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junimoDatabase.blueprint')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junimoDatabase.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junimoDatabase.character')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junimoDatabase.resource')),
            ],
        ),
    ]