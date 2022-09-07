from cgitb import strong
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from UserAppFinal.forms import *


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
                messages.success(request, 'Inicio de sesion satisfactorio!')
            else:
                messages.info(request, 'Inicio de sesión fallido. Verifique Usuario y Contraseña')
        else:
            messages.error(request, 'inicio de sesion fallido!')

        return redirect('App_Final_Inicio')

    contexto = {
        'form': AuthenticationForm(),
        'name_form': 'Iniciar Sesión'
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
        'name_form': 'Registro'
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)