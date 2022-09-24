# Generated by Django 4.1.1 on 2022-09-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0003_socio_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='fecha_alta',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='socio',
            name='fecha_baja',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
