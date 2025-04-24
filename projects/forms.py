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
        widget = forms.SelectMultiple(attrs={
            'class': 'form-control select2-field',
            "data-api-url": "/api/task-list/",
            "data-q": "title",
            'data-text': 'title'    
        })
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'status', 'priority', 'task_list', 'due_date']