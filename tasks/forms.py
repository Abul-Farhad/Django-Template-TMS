from django import forms
from accounts.models import CustomUser
from projects.models import Project
from tasks.models import Task

class TaskForm(forms.ModelForm):
  

    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'})
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description'})
    )

    assigned_to = forms.ModelChoiceField(
        queryset=CustomUser.objects.none(),  # Replace with your CustomUser model's queryset
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control select2-field',
            "data-api-url": "/api/user-list/",
            "data-q": "email",
            'data-text': 'email'
            })
    )
 
    project = forms.ModelChoiceField(
        queryset=Project.objects.none(),  # Replace with your Project model's queryset
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control select2-field',
            "data-api-url": "/api/project-list/",
            "data-q": "title",
            'data-text': 'title'
            })
    )
    status = forms.ChoiceField(
        choices=Task.STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    priority = forms.ChoiceField(
        choices=Task.PRIORITY_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    due_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})
    )
    created_at = forms.DateTimeField(required=False)
    updated_at = forms.DateTimeField(required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'assigned_to', 'project', 'due_date']




