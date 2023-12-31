from django.db import models

# Create your models here.
class Autos(models.Model):
    marca = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    anio = models.IntegerField(null=False, blank=False )
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca},{self.version}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    mail = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre},{self.apellido}"

class Vendedores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    legajo = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return f"{self.nombre},{self.apellido}"