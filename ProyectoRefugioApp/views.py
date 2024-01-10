from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

from mascotas.models import Mascota

# Create your views here.

def home(request):

	return render(request, "ProyectoRefugioApp/home.html")

############################################
#def ayudar(request):

	#return render(request, "ProyectoRefugioApp/home.html")

def ayudardonar(request):

	return render(request, "ProyectoRefugioApp/ayudardonar.html")

def ayudarapadrinar(request):

	return render(request, "ProyectoRefugioApp/ayudarapadrinar.html")

def ayudarapadrinarformulario(request):

	return render(request, "ProyectoRefugioApp/ayudarapadrinarformulario.html")

##########################################
def ayudarvoluntarios(request):

	return render(request, "ProyectoRefugioApp/ayudarvoluntarios.html")

def ayudarsocio(request):

	return render(request, "ProyectoRefugioApp/ayudarsocio.html")
###########################################
# def adoptar(request):

# 	return render(request, "ProyectoRefugioApp/adoptar.html")

# def adoptarformulario(request):

# 	return render(request, "ProyectoRefugioApp/adoptarformulario.html")
###########################################
