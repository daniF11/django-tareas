from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def inicio(request):
    return HttpResponse("Máquina, tu proyecto ya está vivo 🔥")

# Create your views here.
from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'base/lista_tareas.html', {'tareas': tareas})


from .forms import TareaForm

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = TareaForm()

    return render(request, 'base/crear_tarea.html', {'form': form})

def toggle_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.completa = not tarea.completa
    tarea.save()
    return redirect('lista')

def editar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    form = TareaForm(instance=tarea)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista')

    return render(request, 'base/editar_tarea.html', {'form': form})

def borrar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.delete()
    return redirect('lista')

