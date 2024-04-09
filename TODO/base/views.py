from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .models import Task
from django.http import JsonResponse


# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'User/home.html')
    
class TodoView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        user_task=Task.objects.filter(user=request.user)
        
        context = {
            'tasks' : user_task
        }
        return render(request, 'User/todo.html',context)
        

class AddTaskView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return render(request,'User/addtask.html')
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed')=='on'
        task = Task.objects.create(title=title, description=description, completed=completed, user=request.user)
        return redirect("base:todo")
        

class CompleteTaskView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()
        return redirect('base:todo')
    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Render your edit task template and pass the task object
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'  # Check if checkbox is checked
        
        # Update the task object
        task.title = title
        task.description = description
        task.completed = completed
        
        # Save changes to the database
        task.save()
        
        # Redirect to the task list page (or any other appropriate page)
        return redirect('base:todo')
    return render(request,'User/edittask.html' , {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('base:todo')