from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.mascota, name="Mascotas"),
    path('adoptar', views.adoptar, name="Adoptar"),
    path('adoptarformulario', views.adoptarformulario, name="AdoptarFormulario"),
    path('acta', views.acta, name="Acta")
]

