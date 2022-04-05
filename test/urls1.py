from django.urls import path, include
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .import views
from .views import TaskListView, TaskView, AttachmentView, TaskListDetail, TaskDetail, AttachmentDetail, TaskListEdit, TaskEdit, AttachmentEdit


app_name = "todo"
urlpatterns = [
    path('tasklists/', TaskListView.as_view(), name= 'tasklists'),
    path('tasks/', TaskView.as_view(), name= 'tasks'),
    path('attachments/', AttachmentView.as_view(), name= 'attachments'),
    
    path('tasklist/<int:pk>', TaskListDetail.as_view(), name= 'tasklist'),
    path('task/<int:pk>', TaskDetail.as_view(), name= 'task'),
    path('attachment/<int:pk>', AttachmentDetail.as_view(), name= 'attachment'),
    
    path('editlist/', TaskListEdit.as_view(), name= 'editlist'),
    path('edittask/', TaskEdit.as_view(), name= 'edittask'),
    path('editattachment/', AttachmentEdit.as_view(), name= 'editattachment'),
    
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),    
]