from django.shortcuts import render
from .models import *

# Create your views here.
def Login(request):
    return render(request, 'Login.html')

def index(request):
    servicios = Servicios.objects.all()
    context = {"servicios":servicios}
    return render(request, 'index.html',context)



# def index(request):
#     alumnos = Alumno.objects.all()
#     context = {"alumnos":alumnos}
#     return render(request, 'index.html', context)