from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [

    # Retrieve task list
    path('portal/', views.task_list, name='task_list'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('save/', views.save, name='save'),
    # Create a task
    path('create/', views.task_create, name='task_create'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),


    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # path('update/', views.task_update, name='task_update'),

    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

]