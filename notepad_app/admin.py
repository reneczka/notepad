from django.contrib import admin
from .models import Note, Task, Todo, Group, Comment, Category

# Register your models here.
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Todo)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Category)

