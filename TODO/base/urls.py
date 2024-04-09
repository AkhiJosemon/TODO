from django.urls import path
from . import views
from .views import HomeView,TodoView,AddTaskView,CompleteTaskView

app_name = 'base'

urlpatterns = [
    path('',HomeView.as_view(),name=''),
    path('home/',HomeView.as_view(),name='home'),
    path('todo/',TodoView.as_view(),name='todo'),
    path('addtask/',AddTaskView.as_view(),name='addtask'),
    path('complete-task/<int:task_id>/', CompleteTaskView.as_view(), name='complete-task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),


]
