from django import forms
# from django.forms import DateInput
from django.contrib.auth.models import User
from .models import Note, Category, TodoList, TodoItem, Team, TeamMember


class NoteForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'my-custom-select'}), required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class': 'my-custom-select'}),
                                  required=False)

    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'team']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoListForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    team = forms.ModelChoiceField(queryset=Team.objects.all(), widget=forms.Select(attrs={'class': 'my-custom-select'}),
                                  required=False)

    class Meta:
        model = TodoList
        fields = ['title', 'team']


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']


class TeamForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))

    class Meta:
        model = Team
        fields = ['name', 'description']


class TeamMemberForm(forms.Form):
    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username does not exist")
        return username


