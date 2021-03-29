from django import forms
from .models import Projects

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = [
            'project_name',
            'project_desc',
            'project_image'
        ]

