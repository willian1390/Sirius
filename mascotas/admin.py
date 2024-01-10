from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.db import models 
from .models import *
# Register your models here.

class MascotaResource(resources.ModelResource):
	class Meta:
		model = Mascota

class MascotaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	readonly_fields=('created','updated')
	#valor = Vacuna.objects.all().aggregate(Sum('precio'))
	list_display=("fecha_recate","nombre_mascota", "lugar_rescate","edad_aprox",
		"sexo","esterilizado", "Vacunas_", "Medicamentos_", "foto",)
	search_fields=["nombre_mascota"]
	list_filter=("lugar_rescate", "fecha_recate",)
	resources_class = MascotaResource

	def foto(self, object):
		return format_html ('<img src={} width="90" height="70" />', object.imagen.url)


class LugarAdmin(admin.ModelAdmin):
	list_display=("nombre_lugar","calle","avenida")
	list_filter=("nombre_lugar",)


class VacunaAdmin(admin.ModelAdmin):
	list_display=("nombre_vacuna","precio")


class MedicamentoAdmin(admin.ModelAdmin):
	list_display=("nombre_medicamento","precio")

#ADOPCIONES DE MASCOTAS
class AdopcionAdmin(admin.ModelAdmin):
	#inlines = (AdopcionInline,)
	search_fields = ["mascota"]
	list_display=("fecha_adopcion","mascota", "nombres_adoptante", "apellidos_adoptante")
	list_filter=("fecha_adopcion",)
	autocomplete_fields = ["mascota"]
	#change_form_template = "rescates/acta.html"

#PUBLICACIONES DE LAS MASCOTAS
class Adoptar_MascotaAdmin(admin.ModelAdmin):

	def foto(self, object):
		return format_html ('<img src={} width="90" height="70" />', object.iadoptar.url)


	list_display=("mascota","foto", "active")
	autocomplete_fields = ["mascota"]
	#search_fields = ["mascota"]
	






admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Raza)
admin.site.register(Vacuna, VacunaAdmin)
admin.site.register(Adopcion, AdopcionAdmin)
admin.site.register(Adoptar_Mascota, Adoptar_MascotaAdmin)