# #-*- coding:utf-8 -*-

# from django.urls import path, re_path
# from . import views

# # namespace
# app_name = 'tasks'

# urlpatterns = [
#     # Create a task
#     path('create/', views.TaskCreateView.as_view(), name='task_create'),
#     # Retrieve task list
#     # path('', views.TaskListView.as_view(), name='task_list'),
#     path('', views.task_list, name='task_list'),
#     # Retrieve single task object
#     re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
#     # Update a task
#     re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
#     # Delete a task
#     re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')

    # # Create a task
    # path('create/', views.task_create, name='task_create'),
    # # Retrieve task list
    # path('', views.task_list, name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

# ]
# tasks/urls.py

from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [

    # Retrieve task list
    path('', views.task_list, name='task_list'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('try1/', views.try1, name='try1'),
    # path('try2/', views.try2, name='try2'),
    # Create a task
    path('create/', views.task_create, name='task_create'),


    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # path('update/', views.task_update, name='task_update'),

    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

]