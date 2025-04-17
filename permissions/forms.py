from django import forms
from .models import Role, Permission

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'permissions']  # Include the name and permissions fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role Name'}),
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Role name is required.")
        return name

    def clean_permissions(self):
        permissions = self.cleaned_data.get('permissions')
        if not permissions:
            raise forms.ValidationError("At least one permission must be selected.")
        return permissions