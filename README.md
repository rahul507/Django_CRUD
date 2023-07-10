# A Simple Example of Django CRUD (Create, Retrieve, Update and Delete) Application Using Functional Based Views

We will use Django and functional based views to develop a simple application to allow one to create a new task, retrieve task list or a single task, update a task and delete a task. 

### create a task app and add it to INSTALLED_APPS

First of all, use `python manage.py startapp tasks` to create a new app named "tasks" and then add it to INSTALLED_APPS in `settings.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
]
```

Then add app urls to project urls.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls'))
]

```

### create Task model and associated form

Our Task model is very simple. We also used ModelForm to create a TaskForm which will then be needed to create or update a task.

### Run your project and test it

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



