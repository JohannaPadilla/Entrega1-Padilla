from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from UserAppFinal.forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.success(request, 'Inicio de sesion satisfactorio. Bienvenido a tu sitio')
            else:
                messages.info(request, 'Inicio de sesión fallido. Verifique Usuario y Contraseña')
        else:
            messages.error(request, 'Inicio de sesion fallo. Intente nuevamente colocando los valores correctos.')

        return redirect('App_Final_Inicio')

    contexto = {
        'form': AuthenticationForm(),
        'name_form': 'Iniciar Sesión',
        'name_submit': 'Ingresar'
    }
    return render(request, 'UserAppFinal/formulario_user.html', contexto)

def registro(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
        
            form.save()
            messages.info(request, 'El usuario fue registrado satisfactoriamente.')
        else:
            messages.info(request, 'El usuario no puedo ser registrado')

        return redirect('App_Final_Inicio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'name_form': 'Registro',
        'name_submit': 'Registrar Usuario'
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)

@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
        
            data = form.cleaned_data()

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.first_name = data.get('first_name')
            usuario.last_name = data.get('last_name')

            usuario.save()

            messages.info(request, 'El usuario fue modificado satisfactoriamente.')
        else:
            messages.info(request, 'El usuario no puedo ser modificado')

        return redirect('App_Final_Inicio')


    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(
            initial={
                'username': usuario.username,
                'email': usuario.email, 
                'first_name': usuario.first_name,
                'last_name': usuario.last_name
            }),
        'name_form': 'Guardar cambios'
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)

def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) == 1:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()

        return redirect("App_Final_Inicio")

    contexto = {
        'form': AvatarForm(),
        'name_form': 'Avatar',
        'name_submit': 'Cargar Avatar'
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)