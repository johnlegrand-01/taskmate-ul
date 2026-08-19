from django import forms
from .models import TaskList

class Taskform(forms.ModelForm):

    class Meta :
        model = TaskList
        fields = ['task','done']

