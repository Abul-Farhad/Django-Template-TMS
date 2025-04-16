from django import forms
from accounts.models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=255,
        
    )
    password = forms.CharField(
        label='Password',
        max_length=128,
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email does not exist.")
        return email
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password is required.")
        return password
    

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='Confirm Password',
        max_length=128,
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password']

        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user