from django import forms
# from django.forms import DateInput

from .models import Note, Category, TodoList, TodoItem


class NoteForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Note
        fields = ['title', 'content', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title']


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']
