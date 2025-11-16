from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm


def lista_tareas(request):
    tareas = Tarea.objects.order_by('-creada_en')
    return render(request, 'tareas/lista.html', {'tareas': tareas})


def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tareas:lista')
    else:
        form = TareaForm()
    return render(request, 'tareas/form.html', {'form': form, 'titulo': 'Nueva tarea'})


def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tareas:lista')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/form.html', {'form': form, 'titulo': 'Editar tarea'})


def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas:lista')
    return render(request, 'tareas/eliminar.html', {'tarea': tarea})


def toggle_completada(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect('tareas:lista')
