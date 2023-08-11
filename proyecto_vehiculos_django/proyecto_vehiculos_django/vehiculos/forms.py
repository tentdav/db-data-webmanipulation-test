from django import forms
from .models import Vehiculo

# Class que procesa la informacion del forms para que lo reciba la base de datos
class VehiculoForms(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["marca", "modelo", "carroceria", "motor", "categoria", "precio"]
        labels = {"marca" : 'Marca:', "modelo" : 'Modelo:', "carroceria" : 'Serial carroceria:', "motor" : 'Serial notor', "categoria" : 'Categoria:', "precio" : 'Precio'}