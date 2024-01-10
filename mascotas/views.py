from django.shortcuts import render
from mascotas.models import Mascota, Adoptar_Mascota, Adopcion

from django.core.paginator import Paginator
# Create your views here.



def mascota(request):

	mascotas=Mascota.objects.filter(active = True)
	paginator = Paginator(mascotas, 10)
	page = request.GET.get('page')
	mascotas = paginator.get_page(page)                           ##nombreVariable : 
	return render(request, "rescates/rescates.html", {"mascotas": mascotas})
	###nombre variable = Clase(Mascota de rescates.models) obtener todos los objetos


def adoptar(request):
	adoptar=Adoptar_Mascota.objects.filter(active = True)
	paginator = Paginator(adoptar, 10)
	page = request.GET.get('page')
	adoptar = paginator.get_page(page)
	return render(request, "rescates/adoptar.html", {"adoptar": adoptar})


def adoptarformulario(request):
 	return render(request, "rescates/adoptarformulario.html")

def acta(request):
	acta=Adoptar_Mascota.objects.filter()
	return render(request, "rescates/acta.html", {"acta": acta})