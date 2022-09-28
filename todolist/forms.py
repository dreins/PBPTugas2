from django.forms import ModelForm
from todolist.models import Task

class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']