# Generated by Django 3.0.8 on 2020-07-04 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=200)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ticker', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PrecioSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_apertura', models.FloatField()),
                ('precio_cierre', models.FloatField()),
                ('precio_maximo', models.FloatField()),
                ('precio_minimo', models.FloatField()),
                ('fecha', models.DateField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acciones.Sector')),
            ],
        ),
        migrations.CreateModel(
            name='PrecioEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_apertura', models.FloatField()),
                ('precio_cierre', models.FloatField()),
                ('precio_maximo', models.FloatField()),
                ('precio_minimo', models.FloatField()),
                ('fecha', models.DateField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acciones.Empresa')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acciones.Sector'),
        ),
    ]
