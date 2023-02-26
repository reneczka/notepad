from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic import ListView


from .models import Category, Note
from .forms import NoteForm, CategoryForm

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
