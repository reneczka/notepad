from django import forms
# from django.forms import DateInput

from .models import Note, Category, Todo


class NoteForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Note
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = '__all__'
#         widgets = {
#             'due_date': DateInput(),
#         }
#

class TodoForm(forms.ModelForm):
    task = forms.CharField(max_length=255)
    due_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Todo
        fields = ['name', 'task', 'due_date']
