from django import forms
# from django.forms import DateInput

from .models import Note, Category


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
