# Generated by Django 4.1.1 on 2022-09-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='correo_electronico',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='socio',
            name='observaciones',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='socio',
            name='provincia',
            field=models.CharField(default='Valencia', max_length=50),
        ),
        migrations.AlterField(
            model_name='socio',
            name='apellidos',
            field=models.CharField(max_length=70, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]