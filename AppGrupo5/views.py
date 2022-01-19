from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
from AppGrupo5.forms import CargaInstrumento
from AppGrupo5.models import Instrumento
import datetime

# Create your views here.

def inicio(request):
    return render(request, "AppGrupo5/inicio.html")

def instrumentos(request):
    return render(request, "AppGrupo5/instrumento.html")

def pedal(request):
    return render(request, "AppGrupo5/pedal.html")

def disco(request):
    return render(request, "AppGrupo5/disco.html")

def Carga_Instrumento(request):

    if request.method == 'POST':

        miformulario = CargaInstrumento(request.POST)

        print(miformulario)

        if miformulario.is_valid:
            
            informacion = miformulario.cleaned_data

            instrumento = Instrumento (marca = informacion ['marca'], modelo =informacion ['modelo'], tipoinstrumento=informacion['tipoinstrumento'],color=informacion['color'])

            instrumento.save()

            return render (request,"AppGrupo5/inicio.html")
    else:

        miformulario = CargaInstrumento()

    return render (request,"AppGrupo5/cargainstrumento.html", {"miformulario":miformulario})


def buscarinstrumento(request):

    if  request.GET["tipoinstrumento"]:

	      
        tipoinstrumento = request.GET['tipoinstrumento'] 
        Instrumentos = Instrumento.objects.filter(tipoinstrumento__icontains=tipoinstrumento)

        return render(request, "AppGrupo5/instrumento.html", {"Instrumentos":Instrumentos,"Tipo de Instrumento":tipoinstrumento})
    else: 

	    respuesta = "No se han cargado ningún dato"

    return HttpResponse(respuesta)
