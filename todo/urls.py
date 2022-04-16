from django.urls import path, include, reverse
from django.conf.urls import include
from django.contrib.sitemaps import views, Sitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps.views import (
     index as site_index_view)
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.conf.urls.static import static

from harvard.sitemaps import sitemaps as sitemaps_dict

from . import views
from .sitemaps import StaticSitemap, TaskListViewSitemap, TaskViewSitemap
from .views import (
    TaskListView, TaskView, AttachmentView, 
    TaskListDetail, TaskDetail, AttachmentDetail, 
    TaskListAdd, TaskAdd, AttachmentAdd, 
    TaskListEdit, TaskEdit, AttachmentEdit, 
    TaskListDelete, TaskDelete, AttachmentDelete,
    settings, contact, about, 
)


app_name = "todo"


sitemaps = {
    'static': StaticSitemap,
    'tasklists': TaskListViewSitemap,
    'tasks': TaskViewSitemap,
}


urlpatterns = [
    path('tasklists/', TaskListView.as_view(), name= 'tasklists'),
    path('tasks/', TaskView.as_view(), name= 'tasks'),
    path('attachments/', AttachmentView.as_view(), name= 'attachments'),
    
    path('addlist/', TaskListAdd.as_view(), name= 'addlist'),
    path('addtask/', TaskAdd.as_view(), name= 'addtask'),
    path('addattachment/', AttachmentAdd.as_view(), name= 'addattachment'),
    
    path('tasklist/<int:pk>', TaskListDetail.as_view(), name= 'tasklist'),
    path('task/<int:pk>', TaskDetail.as_view(), name= 'task'),
    path('attachment/<int:pk>', AttachmentDetail.as_view(), name= 'attachment'),
    
    path('editlist/<int:pk>', TaskListEdit.as_view(), name= 'editlist'),
    path('edittask/<int:pk>', TaskEdit.as_view(), name= 'edittask'),
    path('editattachment/<int:pk>', AttachmentEdit.as_view(), name= 'editattachment'),
    
    path('deletelist/<int:pk>', TaskListDelete.as_view(), name= 'deletelist'),
    path('deletetask/<int:pk>', TaskDelete.as_view(), name= 'deletetask'),
    path('deleteattachment/<int:pk>', AttachmentDelete.as_view(), name= 'deleteattachment'),
    
    path('settings/', views.settings, name= 'settings'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('terms-conditions/', views.contact, name= 'terms'),
    
    path('sitemap/', site_index_view, {'sitemaps': sitemaps_dict, 'template_name': 'sitemap.html'}, name='sitemap.index'),
    path('sitemaps/', sitemap, {'sitemaps': sitemaps, 'template_name':'sitemaps.html', 'template_name': 'sitemaps.html'}, name='django.contrib.sitemaps.views.sitemap')    
]

