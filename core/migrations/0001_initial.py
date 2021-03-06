# Generated by Django 3.2.4 on 2021-07-06 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idpais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrePais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Periodista',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('contraseña', models.CharField(max_length=50)),
                ('pais', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pais')),
            ],
        ),
    ]
