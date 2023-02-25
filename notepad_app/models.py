from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    group_members = models.ManyToManyField(User, related_name='group_members')

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class Todo(models.Model):
    name = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    due_date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
