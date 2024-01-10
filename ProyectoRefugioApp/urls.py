from django.urls import path

from ProyectoRefugioApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),
   # path('ayudar', views.ayudar, name="Ayudar"),
    path('ayudardonar', views.ayudardonar, name="AyudarDonar"),

    path('ayudarapadrinar', views.ayudarapadrinar, name="AyudarApadrinar"),
    path('ayudarapadrinarformulario', views.ayudarapadrinarformulario, name="AyudarApadrinarFormulario"),

    path('ayudarvoluntarios', views.ayudarvoluntarios, name="AyudarVoluntarios"),
    path('ayudarsocio', views.ayudarsocio, name="AyudarSocio"),

    # path('adoptar', views.adoptar, name="Adoptar"),
    # path('adoptarformulario', views.adoptarformulario, name="AdoptarFormulario"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 