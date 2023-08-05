from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def autos(request):
    ctx = { "autos": Autos.objects.all()}
    return render(request, "aplicacion/autos.html", ctx)

def clientes(request):
    ctx = { "clientes":  Clientes.objects.all(),}
    return render(request, "aplicacion/clientes.html", ctx)

def buscarClientes(request):
    if request.method == 'GET':
        form = ClienteForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            dni = form.cleaned_data['dni']
            mail = form.cleaned_data['mail']

            clientes = Clientes.objects.filter(nombre__icontains=nombre, apellido__icontains=apellido, dni__icontains=dni, mail__icontains=mail)
        else:
            clientes = Clientes.objects.all()
    else:
        form = ClienteForm()
        clientes = Clientes.objects.all()

    return render(request, 'aplicacion/buscarClientes.html', {'form': form, 'clientes': clientes})


def vendedores(request):
    ctx = { "clientes":  Vendedores.objects.all(),}
    return render(request, "aplicacion/vendedores.html", ctx )




def autoForm (request):
    if request.method == "POST":
        auto = Autos(marca=request.POST['marca'], version=request.POST['version'])
        auto.save()
        return HttpResponse("Se grabo con exito el Vehiculo")
    
    return render(request, "aplicacion/autoForm.html")

def autoForm2 (request):
    if request.method == "POST":
        miForm = AutoForm(request.POST)
        print ( miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            auto = Autos(marca=informacion['marca'], version=informacion['version'],anio=informacion['año'],color=informacion['color'] )
            auto.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = AutoForm()

    return render(request, "aplicacion/autoForm2.html",{"form":miForm})

def buscarMarca(request):
    return render(request, "aplicacion/buscarMarca.html")

def buscar2(request):
    marca = request.GET.get("marca", "") 
    autos = Autos.objects.filter(marca__icontains=marca)

    context = {
        "marca": marca, 
        "autos": autos,  
    }

    return render(request, "aplicacion/resultadosMarca.html", context)



