from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rosa
from .form import RosaForm

# Create your views here.

# vistas generales
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


# CRUD de capullos
def capullo(request):
    rosas = Rosa.objects.all()
    return  render(request, "capullos/index.html", {'rosas': rosas})

def crea_capullo(request):
    formulario = RosaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("las_flores")
    return render(request, "capullos/crear.html", {'formulario': formulario})

def editar_capullo(request, pk):
    rosas = Rosa.objects.get(id=pk)
    formulario = RosaForm(request.POST or None, request.FILES or None, instance=rosas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("las_flores")
    return render(request, "capullos/editar.html", {'formulario': formulario})

def eliminar_capullo(request, id):
    rosa = Rosa.objects.get(id = id)
    rosa.delete()
    return redirect("las_flores")


