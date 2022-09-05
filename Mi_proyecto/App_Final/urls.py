from django.urls import path
from App_Final.views import *

urlpatterns = [
    path('', inicio, name='App_Final_Inicio'),
    path('contacto/', contacto, name='Contacto'),
    path('terminos/', terminos, name='terminos'),
    path('privacidad/', privacidad, name='privacidad'),
    path('acerca/', acerca, name='acerca'),
    path('anime_formulario/', animeformulario, name='anime_form'),
    path('autor_formulario/', autorformulario, name='autor_form'),
    path('genero_formulario/', generoformulario, name='genero_form'),
    path('mostrar_anime/', mostrar_anime, name='mostrar_anime'),
    path('mostrar_autor/', mostrar_autor, name='mostrar_autor'),
    path('mostrar_genero/', mostrar_genero, name='mostrar_genero'),
    path('buscar_anime_get/', buscar_anime_get, name='buscar_anime_get'),
    path('buscar_anime/', buscar_anime, name='buscar_anime'),
    path('eliminar_anime/<str:titulo>', eliminar_anime, name='eliminar_anime'),
    path('eliminar_autor/<str:nombre>', eliminar_autor, name='eliminar_autor'),
    path('eliminar_genero/<str:nombre>', eliminar_genero, name='eliminar_genero'),
    path('editar_anime/<str:titulo>', editar_anime, name='editar_anime')
]