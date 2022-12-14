# Generated by Django 4.1 on 2022-08-24 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JunimoDatabaseApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resource',
            new_name='Material',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='resource_id',
            new_name='material_id',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='resource_description',
            new_name='material_description',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='resource_image',
            new_name='material_image',
        ),
        migrations.RenameField(
            model_name='material',
            old_name='resource_name',
            new_name='material_name',
        ),
        migrations.RenameField(
            model_name='recipematerial',
            old_name='resource_id',
            new_name='material_id',
        ),
    ]
