from django.shortcuts import get_object_or_404, render, redirect
from .models import TaskModel
from .forms import TaskForm

# Create your views here.

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('show_tasks')
    return render(request, 'delete_task.html', {'task': task})

def complete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')

def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})
