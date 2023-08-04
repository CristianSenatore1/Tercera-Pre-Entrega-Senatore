from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('',index, name='Inicio' ),

    path('vendedores/', vendedores , name="vendedores"),
    path('autos/', autos , name="autos"),
    path('clientes/', clientes , name="clientes"),

    path('autoForm/', autoForm , name="autoForm"),
    path('autoForm2/', autoForm2, name="autoform2"),

    path('buscarMarca/', buscarMarca, name="marca"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscarClientes/', views.buscarClientes, name='buscar_clientes'),



    
]
