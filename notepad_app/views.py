from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Note, TodoList, TodoItem
from .forms import NoteForm, CategoryForm, TodoListForm, TodoItemForm


# Create your views here

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


login_view = auth_views.LoginView.as_view(template_name='login.html')
logout_view = auth_views.LogoutView.as_view(template_name='logout.html')


def index(request):
    categories = Category.objects.all()
    notes = Note.objects.all()
    return render(request, 'base.html', {'categories': categories, 'notes': notes})


@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)  # only notes for the logged-in user
    return render(request, 'note_list.html', {'notes': notes})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})


@login_required()
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


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')


@login_required
def notes_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    notes = Note.objects.filter(category=category)
    return render(request, 'notes_by_category.html', {'category': category, 'notes': notes})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})


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


@login_required()
def todo_lists(request):
    todo_lists = TodoList.objects.filter(user=request.user)
    return render(request, 'todo_lists.html', {'todo_lists': todo_lists})


@login_required
def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    return render(request, 'create_todo_list.html', {'form': form})


@login_required
def update_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, id=pk)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'update_todo_list.html', {'form': form, 'todo_list': todo_list})


@login_required
def delete_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, id=pk)
    if request.method == 'POST':
        todo_list.delete()
        return redirect('todo_lists')
    return render(request, 'delete_todo_list.html', {'todo_list': todo_list})


@login_required()
def todo_list_detail(request, pk):
    todo_list = get_object_or_404(TodoList, pk=pk)
    todo_items = TodoItem.objects.filter(todo_list=todo_list)

    if request.method == 'POST':
        for todo_item in todo_items:
            checkbox_name = f'todo_item_{todo_item.id}'
            checkbox_value = request.POST.get(checkbox_name)
            if checkbox_value:
                todo_item.completed = True
            else:
                todo_item.completed = False
            todo_item.save()

        return redirect('todo_list_detail', pk=todo_list.id)

    return render(request, 'todo_list_detail.html', {'todo_list': todo_list, 'todo_items': todo_items})


def create_todo_item(request, pk):
    todo_list = get_object_or_404(TodoList, id=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.todo_list = todo_list
            todo_item.save()
            return redirect('todo_list_detail', pk=todo_list.id)
    else:
        form = TodoItemForm()
    return render(request, 'create_todo_item.html', {'form': form, 'todo_list': todo_list})


def update_todo_item(request, pk):
    todo_item = get_object_or_404(TodoItem, id=pk)
    todo_list = todo_item.todo_list
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.completed = request.POST.get('completed') == 'on'
            todo_item.save()
            return redirect('todo_list_detail', pk=todo_list.id)
    else:
        form = TodoItemForm(instance=todo_item)
    return render(request, 'update_todo_item.html', {'form': form, 'todo_item': todo_item})


def delete_todo_item(request, pk):
    todo_item = get_object_or_404(TodoItem, id=pk)
    todo_list = todo_item.todo_list
    if request.method == 'POST':
        todo_item.delete()
        return redirect('todo_list_detail', pk=todo_list.id)
    return render(request, 'delete_todo_item.html', {'todo_item': todo_item, 'todo_list': todo_list})


