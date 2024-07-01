from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full h-32'}),
            'status': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
            'priority': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
            'due_date': forms.DateInput(attrs={'class': 'form-input mt-1 block w-full', 'type': 'date'}),
            'category': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
        }
