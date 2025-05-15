from django import forms
from .models import Project
from django.forms import DateInput

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
                    'start_date': forms.DateInput(attrs={'type': 'date'}),
                    'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
            