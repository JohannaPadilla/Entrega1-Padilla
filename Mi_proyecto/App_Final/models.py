from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.
class Autor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Nacionalidad: {self.nacionalidad} - Fecha de creacion: {self.fecha_creacion}"

class Genero(models.Model):
    
    nombre = models.CharField(max_length=40)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de creacion: {self.fecha_creacion}"

class Anime(models.Model):
    
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length= 40)
    fecha_de_creacion = models.DateField()
    episodios = models.IntegerField()
    temporadas = models.IntegerField()
    origen = models.CharField(max_length=40)
    genero = models.CharField(max_length=15)
    personaje_principal = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=2000)
    fecha_creacion = models.DateField(auto_now=True)
    puntuacion = models.IntegerField()

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor {self.autor} - Episodios: {self.episodios} - Fecha de creacion: {self.fecha_creacion} - Temporadas: {self.temporadas} - Origen: {self.origen} - Genero: {self.genero} - Personaje Principal: {self.personaje_principal} - Sinopsis: {self.sinopsis} - Fecha de lanzamiento: {self.fecha_de_creacion} -  Puntuacion: {self.puntuacion}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    fecha_de_nacimiento = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Nacionalidad: {self.nacionalidad} - Fecha de creacion: {self.fecha_creacion} -  Fecha de nacimiento: {self.fecha_de_nacimiento} -  Email: {self.email} -  Password: {self.password}"