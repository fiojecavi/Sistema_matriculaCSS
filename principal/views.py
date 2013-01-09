# Create your views here.
from principal.models import Alumno, Profesor, Curso, Matricula, Dictar, Nota
from django.shortcuts import render_to_response

def lista_alumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('lista_alumnos.html',{'alumnos':alumnos})

def lista_cursos(request):
	cursos = Curso.objects.all()
	return render_to_response('lista_cursos.html',{'cursos':cursos})

def lista_profesores(request):
	profesores = Profesor.objects.all()
	return render_to_response('lista_profesores.html',{'profesores':profesores})

def dato_alumno(request, id_alumno):	
	dato= Alumno.objects.get(pk=id_alumno)
	return render_to_response('dato_alumno.html',{'alumno':dato})




