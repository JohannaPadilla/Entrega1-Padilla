from django.shortcuts import render, redirect
from App_Final.models import *
from App_Final.forms import *
from django.contrib import messages
import django
from django.contrib.auth.decorators import login_required



# Create your views here.

# Vistas simples
def inicio(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'App_Final/contacto.html', contexto)

def terminos(request):
    contexto = {}
    return render(request, 'App_Final/terminos.html', contexto)

def privacidad(request):
    contexto = {}
    return render(request, 'App_Final/privacidad.html', contexto)

def acerca(request):
    contexto = {}
    return render(request, 'App_Final/acerca.html', contexto)

# Vistar de formularios
@login_required
def animeformulario(request):

    if request.method == 'POST':
        mi_formulario = Animeform(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            anime_1 = Anime(titulo=data.get('titulo'),
                          autor=data.get('autor'),
                          fecha_de_creacion=data.get('fecha_de_creacion'),
                          episodios=data.get('episodios'),
                          temporadas=data.get('temporadas'),
                          origen=data.get('origen'),
                          genero=data.get('genero'),
                          personaje_principal=data.get('personaje_principal'),
                          sinopsis=data.get('sinopsis'),
                          puntuacion=data.get('puntuacion'))
            anime_1.save()
            
            return redirect('anime_form')

    contexto = {
        'form': Animeform(),
        'name_submit': 'Ingreso Anime'
    }

    return render(request, 'App_Final/formulario_general.html', contexto)

@login_required
def autorformulario(request):

    if request.method == 'POST':
        mi_formulario = Autorform(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            autor_1 = Autor(nombre=data.get('nombre'),
                          apellido=data.get('apellido'),
                          nacionalidad=data.get('nacionalidad'))
            autor_1.save()

            return redirect('autor_form')

    contexto = {
        'form': Autorform(),
        'name_submit': 'Ingreso Autor'
    }

    return render(request, 'App_Final/formulario_general.html', contexto)

@login_required
def generoformulario(request):

    if request.method == 'POST':
        mi_formulario = Generoform(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            genero_1 = Genero(nombre=data.get('nombre'))
            genero_1.save()

            return redirect('genero_form')

    contexto = {
        'form': Generoform(),
        'name_submit': 'Ingreso Genero'
    }

    return render(request, 'App_Final/formulario_general.html', contexto)

# Mostrando datos de DB
def mostrar_anime(request):

    animes = Anime.objects.all()

    contexto = {
        'animes': animes
    }

    return render(request, 'App_Final/mostrar_anime.html', contexto)

def mostrar_autor(request):

    autores = Autor.objects.all()

    contexto = {
        'autores': autores
    }

    return render(request, 'App_Final/mostrar_autor.html', contexto)

def mostrar_genero(request):

    generos = Genero.objects.all()

    contexto = {
        'generos': generos
    }

    return render(request, 'App_Final/mostrar_genero.html', contexto)

# Busqueda de datos
def buscar_anime_get(request):
    titulo = request.GET.get('titulo')

    animes = Anime.objects.filter(titulo__icontains=titulo)

    contexto ={
        'animes': animes
    }

    return render(request, 'App_Final/mostrar_anime.html', contexto)

def buscar_anime(request):
    
    contexto = {
        'form': Animebuscarform()
    }

    return render(request, 'App_Final/buscar_anime.html', contexto)

# Eliminar Datos
@login_required
def eliminar_anime(request, titulo):

    anime_eliminar = Anime.objects.get(titulo=titulo)
    anime_eliminar.delete()

    messages.info(request, f"El anime {anime_eliminar.titulo} fue eliminado con exito")

    return redirect("mostrar_anime")

@login_required
def eliminar_autor(request, nombre):

    autor_eliminar = Autor.objects.get(nombre=nombre)
    autor_eliminar.delete()

    messages.info(request, f"El autor {autor_eliminar.nombre} fue eliminado con exito")

    return redirect("mostrar_autor")

@login_required
def eliminar_genero(request, nombre):

    genero_eliminar = Genero.objects.get(nombre=nombre)
    genero_eliminar.delete()

    messages.info(request, f"El genero {genero_eliminar.nombre} fue eliminado con exito")

    return redirect("mostrar_genero")

# Editar Datos
@login_required
def editar_anime(request, titulo):
    anime_editar = Anime.objects.get(titulo=titulo)

    if request.method == 'POST':
        mi_formulario = Animeform(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            anime_editar.titulo = data.get('titulo')
            anime_editar.autor = data.get('autor')
            anime_editar.fecha_de_creacio = data.get('fecha_de_creacion')
            anime_editar.episodios = data.get('episodios')
            anime_editar.temporadas = data.get('temporadas')
            anime_editar.origen = data.get('origen')
            anime_editar.genero = data.get('genero')
            anime_editar.personaje_principal = data.get('personaje_principal')
            anime_editar.sinopsis = data.get('sinopsis')
            anime_editar.puntuacion = data.get('puntuacion')
            try:
                anime_editar.save()
                messages.info(request, f"El anime {anime_editar.titulo} fue editado con exito")
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion fallo por que en anime ya existe")

            return redirect('mostrar_anime')


    contexto = {
        'form': Animeform(
            initial={
                "titulo": anime_editar.titulo,
                "autor": anime_editar.autor,
                "fecha_de_creacion": anime_editar.fecha_de_creacion,
                "episodios": anime_editar.episodios,
                "temporadas": anime_editar.temporadas,
                "origen": anime_editar.origen,
                "genero": anime_editar.genero,
                "personaje_principal": anime_editar.personaje_principal,
                "sinopsis": anime_editar.sinopsis,
                "puntuacion": anime_editar.puntuacion
            }
        )
    }


    return render(request, 'App_Final/anime_formulario.html', contexto)