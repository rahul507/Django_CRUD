# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse, reverse_lazy
# from .models import Task
# from .forms import TaskForm

# # Create your views here.
# # Functional based view
# # Create a task
# def task_create(request):
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("tasks:task_list"))
#     else:
#         form = TaskForm()

#     return render(request, "tasks/task_form.html", { "form": form, })
# #
# #
# # # Retrieve task list
# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, "task_list.html", { "tasks": tasks,})
# #
# #
# # # Retrieve a single task
# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, "tasks/task_detail.html", { "task": task, })
# #
# #
# # # Update a single task
# def task_update(request, pk):
#     task_obj = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(instance=task_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("tasks:task_detail", args=[pk,]))
#     else:
#         form = TaskForm(instance=task_obj)

#     return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})
# #
# #
# # # Delete a single task
# def task_delete(request, pk):
#     task_obj = get_object_or_404(Task, pk=pk)
#     task_obj.delete()
#     return redirect(reverse("tasks:task_list"))

# # Class Based Views
# from django.views.generic import ListView, DetailView, \
#     CreateView, UpdateView, DeleteView

# class TaskListView(ListView):
#     model = Task
#     context_object_name = 'tasks'

# class TaskDetailView(DetailView):
#     model = Task

# class TaskCreateView(CreateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy('tasks:task_list')

# class TaskUpdateView(UpdateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy('tasks:task_list')

# class TaskDeleteView(DeleteView):
#     model = Task
#     success_url = reverse_lazy('tasks:task_list')


# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from .forms import MyForm
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

# Create a task
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_list"))
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", { "form": form, })
def try1(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['driver_email']
            password=form.cleaned_data['driver_password']
            print(email)
            entries = Task.objects.filter(email=email,password=password)
            if(entries):
                print(entries)
                task_obj = get_object_or_404(Task, email=email,password=password)
                print(task_obj)
                task_obj.delete()
                # entries.delete()
                return redirect(reverse("tasks:task_list"))
                
            else:
                
                form=MyForm()
            
    else:
        form = MyForm()

    return render(request, "delete.html", { "form": form, })




# Retrieve task list
def task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, "tasks/task_list.html", { "tasks": tasks,})
def index(request):
    return render(request, "index.html")
def home(request):
    return render(request, "home.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return render(request,'home.html')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request,'home.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return render(request,'home.html')



# Retrieve a single task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print("anythng")
    return render(request, "tasks/task_detail.html", { "task": task, })


# Update a single task
def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk,]))
    else:
        form = TaskForm(instance=task_obj)

    return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})



# Delete a single task
def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    return redirect(reverse("tasks:task_list"))
