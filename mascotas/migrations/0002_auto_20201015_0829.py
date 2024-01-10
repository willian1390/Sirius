# Generated by Django 2.2.5 on 2020-10-15 14:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptar_mascota',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='adoptar_mascota',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Descripcion de mascota'),
        ),
    ]
