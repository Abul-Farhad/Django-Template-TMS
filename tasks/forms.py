from django import forms

class TaskForm(forms.Form):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Title'})
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description'})
    )
    assigned_to = forms.CharField(
        required=True,
        widget=forms.HiddenInput(attrs={
            'class': 'form-control select2-field',
            'data-api-url': '/api/user-list/',
            'placeholder': 'Assigned To',
            'id': 'assigned_to'
        })
    )
    project = forms.CharField(
        required=True,
        widget=forms.HiddenInput(attrs={
            'class': 'form-control select2-field',
            'data-api-url': '/api/task-list/',
            'placeholder': 'Project',
            'id': 'project'
        })
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    due_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})
    )
    created_at = forms.DateTimeField(required=False)
    updated_at = forms.DateTimeField(required=False)
