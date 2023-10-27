from django.shortcuts import render
# from .models import user
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.

# def create_user(request):
#     user(usuario=request.POST['usuario'], email=request.POST['email'])
#     user.save
#     print(request.POST)

def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html')
    else:

        if request.POST['contraseña1'] == request.POST['contraseña2']:
            try:
                user = User.objects.create_user(username=request.POST['usuario'], password=request.POST['contraseña1'])
                user.save()
                return HttpResponse('Usuario creado satisfactoriamente')
            except IntegrityError:
                return render(request, 'registro.html', {"error": "El usuario ya existe."})
        
        else:
            return (request, 'registro.html', {"error": "Las contraseñas no coinciden."})
        
