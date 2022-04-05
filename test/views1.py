from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.db import migrations, models
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


from .models import *


time=["5:00 a.m.", "5:15 a.m.", "5:30 a.m.", "5:45 a.m.", "6:00 a.m.", "6:15 a.m.", "6:30 a.m.", "6:45 a.m.", "7:00 a.m.", "7:15 a.m.", "7:30 a.m.", "7:45 a.m.", "8:00 a.m.", "8:15 a.m.", "8:30 a.m.", "8:45 a.m.", "9:00 a.m.", "9:15 a.m.", "9:30 a.m.", "9:45 a.m.", "10:00 a.m.", "10:15 a.m.", "10:30 a.m.", "10:45 a.m.", "11:00 a.m.", "11:15 a.m.", "11:30 a.m.", "11:45 a.m.","12:00 a.m.", "12:15", "12:30", "12:45",  "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "1:00 a.m.", "1:15 a.m.", "1:30 a.m.", "1:45 a.m.", "2:00 a.m.", "2:15 a.m.", "2:30 a.m.", "2:45 a.m.", "3:00 a.m.", "3:15 a.m.", "3:30 a.m.", "3:45 a.m.", "4:00 a.m.", "4:15 a.m.", "4:30 a.m.", "4:45 a.m."]

class TaskListView(ListView):
	model= List
	template_name= 'todo/tasklists.html'
	
	def __str__(self):
		return '__all__'
	
class TaskView(ListView):
	model= Task
	template_name= 'todo/tasks.html'
	
	def __str__(self):
		return ['title', 'task_list.name', 'priority', 'status', 'str(id) ',  'completed']
	
class AttachmentView(ListView):
	model= Attachment
	template_name= 'todo/attachments.html'
	
class TaskListDetail(DetailView):
	model= List
	template_name= 'todo/tasklist.html'
	slug_url_kwarg= 'pk'
	slug_field='pk'
	
	def get_success_url(self):
		return reverse_lazy('tasklist', kwargs=[self.id])	
	
class TaskDetail(DetailView):
	model= Task
	template_name= 'todo/task.html'
	slug_url_kwarg= 'pk'
	slug_field='pk'
	
	def get_success_url(self):
		return reverse_lazy('task', kwargs=[self.id])
	
class AttachmentDetail(DetailView):
	model= Attachment
	template_name= 'todo/attachment.html'
	slug_url_kwarg= 'pk'
	slug_field='pk'
	
	def get_success_url(self):
		return reverse_lazy('attachment', kwargs=[self.id])
	
class TaskListEdit(CreateView):
	model= List
	template_name= 'todo/editlist.html'
	fields= '__all__'
	
	def get_absolute_url(self):
		return reverse('todo/editlist')
	
class TaskEdit(CreateView):
	model= Task
	template_name= 'todo/edittask.html'
	fields= '__all__'
	
class AttachmentEdit(CreateView):
	model= Attachment
	template_name= 'todo/editattachment.html'
	fields= '__all__'

# Create your views here
def tasks(request):
    messages.success(request, ('Task has been added to your List successfully!'))
    return render(request, 'todo/tasks.html', {
            "form": form, "todo": todo, "time": time,
    }) #reloading the page
    		  
def about(request):	
    return render(request, 'todo/about.html', {})	

def contact(request):	
    my_name= "Maricla Martelli Kandzorra"	
    return render(request, 'todo/contact.html', {
        'name': my_name
    })