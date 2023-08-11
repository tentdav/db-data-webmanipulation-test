from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoForms
# Create your views here.


# View de la home page
def index_view(request):
    return render(request, 'index.html')


# View que llama a la pagina que lista los vehiculos, y guarda la informacion del forms a la pagina. Dato curioso, estuve peleando un dia entero con esta view ya que no guardaba la informacion del forms, y era porque me faltaba un parentesis XD
def add_view(request):
    if request.method == "POST":                         
            form = VehiculoForms(request.POST or None)
            if form.is_valid:
                form.save()
                return render(request, 'add.html')
    else:
         return render(request, 'add.html')


# lista a llama a la informacion de la base de datos
def list_view(request):
    lista = Vehiculo.objects.all
    return render(request, 'list.html', {'todo': lista})
