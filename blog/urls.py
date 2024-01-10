from django.urls import path
from .import views


urlpatterns = [
    path('', views.blog, name="Blog"),
    path('blogleer', views.blogleer, name="BlogLeer"),
    path('categoria/<categoria_id>/', views.categoria, name="Categoria"),
    path('blogleer', views.blogleer, name="BlogLeer"),

]
