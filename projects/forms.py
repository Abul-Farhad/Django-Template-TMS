import json
from django import forms
from projects.models import Project
from tasks.models import Task

class ProjectForm(forms.ModelForm):
    
    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'})
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description'})
    )
    priority = forms.ChoiceField(
        choices=Project.PRIORITY_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    status = forms.ChoiceField(
        choices=Project.STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    due_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})
    )
    created_at = forms.DateTimeField(required=False)
    updated_at = forms.DateTimeField(required=False)
    task_list = forms.ModelMultipleChoiceField(
        queryset = Task.objects.none(),
        required=False,
        widget = forms.SelectMultiple()
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'status', 'priority', 'due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        config = {
            "apiUrl": "/api/task-list/",
            "queryParam": "title",
            "textField": "title",
            "filters": {
                "task_assigned_to_project": False  # False means tasks with no project and True means tasks with project
            }
        }

        self.fields['task_list'].widget.attrs.update({
            'class': 'form-control select2-field',
            'data-config': json.dumps(config)
        })


    def save(self, commit = ...):
        task_list = self.cleaned_data.pop('task_list')
        project = super().save(commit=commit)
        if task_list:
            Task.objects.filter(id__in=task_list).update(project=project)
        
        return project