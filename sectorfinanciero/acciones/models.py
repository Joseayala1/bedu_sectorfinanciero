from django.db import models

# Create your models here.

class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    ticker =  models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    ticker =  models.CharField(max_length=200)
    nacionalidad =  models.CharField(max_length=100)
    descripcion =  models.TextField()
    sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, null=True)

class PrecioEmpresa(models.Model):
    precio_apertura = models.FloatField()
    precio_cierre = models.FloatField()
    precio_maximo = models.FloatField()
    precio_minimo = models.FloatField()
    fecha = models.DateField()
    empresa =  models.ForeignKey(Empresa,on_delete=models.CASCADE)

class PrecioSector(models.Model):
    precio_apertura = models.FloatField()
    precio_cierre = models.FloatField()
    precio_maximo = models.FloatField()
    precio_minimo = models.FloatField()
    fecha = models.DateField()
    sector =  models.ForeignKey(Sector,on_delete=models.CASCADE)





    
