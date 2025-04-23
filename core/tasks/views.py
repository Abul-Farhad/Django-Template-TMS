from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from tasks.models import Task
from tasks.forms import TaskForm

class ListTasksView(View):
    form = TaskForm()
    def get(self, request):
        return render(request, 'tasks.html', {"form": self.form})
    
class CreateTaskView(View):
    form = TaskForm()
    def get(self, request):
        return render(request, 'create_task.html', {"form": self.form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('create_task')
        else:
            messages.error(request, 'Error creating task.')
        return render(request, 'create_task.html', {"form": self.form})