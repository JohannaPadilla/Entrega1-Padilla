from atexit import register
from django.urls import path
from UserAppFinal.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login_appfinal'),
    path('registro/', registro, name='register_appfinal'),
    path('salir/', LogoutView.as_view(template_name='UserAppFinal/salir.html'), name='salir_UserAppFinal'),
    path('editar/', editar_usuario, name='editar_usuario'),
    path('avatar/', upload_avatar, name='cargar_avatar')
]