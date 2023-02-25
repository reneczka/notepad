from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic import ListView


from .models import Category, Group, Note, Comment, Todo
from .forms import NoteForm, CategoryForm, TodoForm

# Create your views here


def index(request):
    categories = Category.objects.all()
    notes = Note.objects.all()
    return render(request, 'base.html', {'categories': categories, 'notes': notes})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})


def note_create(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    return render(request, 'note_form.html', {'form': form})


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')


def notes_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    notes = Note.objects.filter(category=category)
    return render(request, 'notes_by_category.html', {'category': category, 'notes': notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    comments = Comment.objects.filter(note=note)
    return render(request, 'note_detail.html', {'note': note, 'comments': comments})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})


def category_update(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories')


def groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    notes = Note.objects.filter(group=group)
    return render(request, 'group_detail.html', {'group': group, 'notes': notes})


# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, 'todo_list.html', {'todos': todos})
#
#
# def todo_create(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todos')
#     else:
#         form = TodoForm()
#     return render(request, 'todo_form.html', {'form': form})
#
#
# def todo_update(request, pk):
#     todo = Todo.objects.get(id=pk)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             return redirect('todos')
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'todo_form.html', {'form': form})
#
#
# def todo_delete(request, pk):
#     Todo.objects.get(id=pk).delete()
#     return redirect('todos')


class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todo_list'


def todo_list_detail(request, todolist_id):
    todolist = get_object_or_404(Todo, pk=todolist_id)
    return render(request, 'todo_list_detail.html', {'todo_list': todolist})


class TodoListCreateView(View):
    form_class = TodoForm
    template_name = 'todo_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect(reverse('todo_list_detail', args=[todo_list.pk]))
        return render(request, self.template_name, {'form': form})


class TodoListUpdateView(View):
    form_class = TodoForm
    template_name = 'todo_form.html'

    def get(self, request, pk, *args, **kwargs):
        todo_list = Todo.objects.get(pk=pk)
        form = self.form_class(instance=todo_list)
        return render(request, self.template_name, {'form': form, 'todo_list': todo_list})

    def post(self, request, pk, *args, **kwargs):
        todo_list = Todo.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo_list_detail', args=[todo_list.pk]))
        return render(request, self.template_name, {'form': form, 'todo_list': todo_list})


class TodoListDeleteView(View):

    def get(self, request, pk, *args, **kwargs):
        todo_list = Todo.objects.get(pk=pk)
        todo_list.delete()
        return redirect(reverse('todo_list'))

