from django import forms

class Autorform(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=40)
  

class Generoform(forms.Form):
    
    nombre = forms.CharField(max_length=40)

class Animeform(forms.Form):

    titulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    fecha_de_creacion = forms.DateField()
    episodios = forms.IntegerField(min_value=1)
    temporadas = forms.IntegerField(min_value=1)
    origen = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=15)
    personaje_principal = forms.CharField(max_length=40)
    sinopsis = forms.CharField(max_length=2000)
    puntuacion = forms.IntegerField(min_value=1, max_value=10)

class Animebuscarform(forms.Form):
    titulo = forms.CharField(max_length=40)

class Usuarioform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=40)
    fecha_de_nacimiento = forms.DateField()
    email = forms.EmailField()
    password = forms.CharField(max_length=50)

