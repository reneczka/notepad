"""notepad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from notepad_app import views
from notepad_app.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('category/<int:category_id>/', views.notes_by_category, name='notes_by_category'),
    path('category/', views.category_list, name='categories'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/update/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('notes/', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/<int:pk>/update/', views.note_update, name='note_update'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('todolist/create/', views.create_todo_list, name='create_todo_list'),
    path('todolist/<int:pk>/update/', views.update_todo_list, name='update_todo_list'),
    path('todolist/<int:pk>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('todoitem/<int:pk>/create/', views.create_todo_item, name='create_todo_item'),
    path('todoitem/<int:pk>/update/', views.update_todo_item, name='update_todo_item'),
    path('todoitem/<int:pk>/delete/', views.delete_todo_item, name='delete_todo_item'),
    path('todolists/', views.todo_lists, name='todo_lists'),
    path('todolist/<int:pk>/', views.todo_list_detail, name='todo_list_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('team/create/', views.team_create, name='team_create'),
    path('team/list/', views.team_list, name='team_list'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('team/<int:pk>/join/', views.team_join, name='team_join'),
    path('team/<int:pk>/leave/', views.team_leave, name='team_leave'),
    path('team/<int:pk>/delete/', views.team_delete, name='team_delete'),
]
