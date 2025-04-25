from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from tasks.models import Task
from tasks.forms import TaskForm
from tasks.serializers import TaskSerializer
from accounts.models import CustomUser
from projects.models import Project

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
        print("####Form Data:", request.POST)
        # Dynamically set the queryset for form fields

        if 'assigned_to' in request.POST:
            try:
                assigned_id = request.POST.get('assigned_to')
                form.fields['assigned_to'].queryset = CustomUser.objects.filter(id=assigned_id)
            except:
                pass
        
        if 'project' in request.POST:
            try:
                project_id = request.POST.get('project')
                form.fields['project'].queryset = Project.objects.filter(id=project_id)
            except:
                pass
        print(form.fields)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('create_task')
        else:
            print("Form Errors:", form.errors)
            messages.error(request, 'Error creating task.')

        return render(request, 'create_task.html', {"form": form})
