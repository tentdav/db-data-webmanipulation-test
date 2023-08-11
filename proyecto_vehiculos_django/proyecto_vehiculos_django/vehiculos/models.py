from django.db import models

# Modelo de la pagina
class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, default='Ford')
    modelo = models.CharField(max_length=100)
    carroceria = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)



    
