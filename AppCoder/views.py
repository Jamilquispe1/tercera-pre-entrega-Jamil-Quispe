from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    
    return render(request,"AppCoder/inicio.html")

def curso(request):

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info["camada"])

            curso.save()

            return render(request, "Appcoder/inicio.html")

    else:

        formulario1 = CursoFormulario()

    return render(request, "AppCoder/curso.html", {"form1":formulario1})


def estudiante(request):

     if request.method == "POST":

        formulario2 = estudianteFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            estudiante = Estudiante(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

            estudiante.save()

            return render(request, "Appcoder/inicio.html")

     else:

        formulario2 = estudianteFormulario()

     return render(request, "AppCoder/estudiantes.html", {"form2":formulario2})

def profesor(request):
    
    if request.method == "POST":

        formulario3 = profesorFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            profesor = Profesore(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])

            profesor.save()

            return render(request, "Appcoder/inicio.html")

    else:

        formulario3 = profesorFormulario()

    return render(request, "AppCoder/profesores.html", {"form3":formulario3})

def entregable(request):
    
    if request.method == "POST":

        formulario4 = entregableFormulario(request.POST)

        if formulario4.is_valid():

            info = formulario4.cleaned_data

            entregable = Entregable(nombre=info["nombre"], fechaEntrega=info["fecha de entrega"])
            entregable.save()

            return render(request, "Appcoder/inicio.html")

    else:

        formulario4 = entregableFormulario()

    return render(request, "AppCoder/entregables.html", {"form4":formulario4})

"""
def cursoFormulario(request):

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info["camada"])

            curso.save()

            return render(request, "Appcoder/inicio.html")

    else:

        formulario1 = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario1})
"""

def busquedaCamada(request):

    return render(request, "AppCoder/inicio.html") 

def resultados(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/inicio.html", {"cursos": cursos, "camada": camada})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)