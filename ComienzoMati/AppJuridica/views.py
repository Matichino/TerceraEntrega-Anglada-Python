from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render (request, "AppJuridica/index.html")

def ServiciosJuridicos (request):
    return render ( request, "AppJuridica/Servicios Juridicos.html")

def ServiciosCiberseguridad(request):
    return render ( request,"AppJuridica/Vista Servicios Ciberseguridad.html")

def Precios(request):
    return render ( request,"AppJuridica/Precios.html")

def SobreNosotros(request):
    return render ( request,"AppJuridica/Sobre Nosotros.html")
