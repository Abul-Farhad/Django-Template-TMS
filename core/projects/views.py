from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from tasks.models import Task
from projects.forms import ProjectForm

class ListProjectView(View):
    form = ProjectForm()
    def get(self, request):
        return render(request, 'projects.html', {"form": self.form})
    
class CreateProjectView(View):
    form = ProjectForm()
    def get(self, request):
        return render(request, 'create_project.html', {"form": self.form})
    
    def post(self, request):
        form = ProjectForm(request.POST)
        print("####Form Data:", request.POST)
        # Dynamically set the queryset for form fields

        if 'task_list' in request.POST:
            tasks_ids = request.POST.getlist('task_list')  # Get multiple task IDs
            form.fields['task_list'].queryset = Task.objects.filter(id__in=tasks_ids)
        
        
        print(form.fields)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, 'Project created successfully.')
            return redirect('create_project')
        else:
            print("Form Errors:", form.errors)
            messages.error(request, 'Error creating task.')

        return render(request, 'create_project.html', {"form": form})
