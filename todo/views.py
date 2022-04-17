from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse, reverse_lazy, Resolver404, resolve, NoReverseMatch
from django.views import generic
from django.template.loader import render_to_string
from django.contrib import messages
from django.db import migrations, models
from django.views.generic import (
    ListView, 
    DetailView, 
    UpdateView,
    DeleteView, 
    CreateView,
)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from harvard.sitemaps import StaticSitemap, TaskListViewSitemap, TaskViewSitemap


from .models import List, Task, Attachment


time=["5:00 a.m.", "5:15 a.m.", "5:30 a.m.", "5:45 a.m.", "6:00 a.m.", "6:15 a.m.", "6:30 a.m.", "6:45 a.m.", "7:00 a.m.", "7:15 a.m.", "7:30 a.m.", "7:45 a.m.", "8:00 a.m.", "8:15 a.m.", "8:30 a.m.", "8:45 a.m.", "9:00 a.m.", "9:15 a.m.", "9:30 a.m.", "9:45 a.m.", "10:00 a.m.", "10:15 a.m.", "10:30 a.m.", "10:45 a.m.", "11:00 a.m.", "11:15 a.m.", "11:30 a.m.", "11:45 a.m.","12:00 a.m.", "12:15", "12:30", "12:45",  "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45", "00:00", "00:15", "00:30", "00:45", "1:00 a.m.", "1:15 a.m.", "1:30 a.m.", "1:45 a.m.", "2:00 a.m.", "2:15 a.m.", "2:30 a.m.", "2:45 a.m.", "3:00 a.m.", "3:15 a.m.", "3:30 a.m.", "3:45 a.m.", "4:00 a.m.", "4:15 a.m.", "4:30 a.m.", "4:45 a.m."]

def upload(request):
    if request.method == 'POST' and request.FILES['addattachment']:
        upload= request.FILES['addattachment']
        fss= FileSystemStorage()
        file= fss.save(upload.name, upload)
        file_url= fss.url(file)
        return render(request, 'todo/attachments.html', {'file.url': file_url})
    return render(request, 'todo/attachments.html')   
    
def index(request):
    return HttpsResponse('todo:index')    
    
#ADD ONE	
class TaskListAdd(CreateView):
	model= List
	template_name= 'todo/addlist.html'
	success_url= reverse_lazy('todo:tasklist')
	fields= '__all__'
	
	def get_absolute_url(self):
		return reverse('todo/tasklist')
	
class TaskAdd(CreateView):
	model= Task
	template_name= 'todo/addtask.html'
	success_url= reverse_lazy('todo:task')
	fields= '__all__'
	
	def get_absolute_url(self):
		return reverse('todo/task')
	
class AttachmentAdd(CreateView):
	model= Attachment
	template_name= 'todo/addattachment.html'
	success_url= reverse_lazy('todo:attachment')
	fields= '__all__'
	
	def get_success_url(self): 
		return reverse('todo:attachment')
		
	

#View all
class TaskListView(ListView):
	model= List
	template_name= 'todo/tasklists.html'
	context_object_name= 'all_lists'
	
	def __str__(self):
		return '__all__'
        
        
	
class TaskView(ListView):
	model= Task
	template_name= 'todo/tasks.html'
	context_object_name= 'all_tasks'
	
	def __str__(self):
		return '__all__'
        
	def get_context_data(self, **kwargs):
		context= super(TaskView, self).get_context_data(**kwargs)
		context['all_objects']= Task.objects.all()
	    
		return context    
	
class AttachmentView(ListView):
	model= Attachment
	template_name= 'todo/attachments.html'
	context_object_name= 'all_attachments'
	
	def __str__(self):
		return '__all__'

#View each		
class TaskListDetail(DetailView):
	model= List
	queryset= List.objects.all()
	template_name= 'todo/tasklist.html'
	context_object_name= 'indiv_list'
	
	def __str__(self):
		return ['title', 'task_list.name', 'priority', 'status', 'str(id) ',  'completed']
		
	def get_context_data(self, **kwargs):
	    context= super(TaskListDetail, self).get_context_data(**kwargs)
	    context['all_objects']= List.objects.all()
	    
	    return context
	
class TaskDetail(DetailView):
	model= Task
	queryset= Task.objects.all()
	template_name= 'todo/task.html'
	context_object_name= 'indiv_task'
	
	def __str__(self):
		return '__all__'
		
	def get_context_data(self, **kwargs):
	    context= super(TaskDetail, self).get_context_data(**kwargs)
	    context['all_objects']= Task.objects.all()
	    
	    return context
	
class AttachmentDetail(DetailView):
	model= Attachment
	queryset= Attachment.objects.all()
	template_name= 'todo/attachment.html' 
	context_object_name= 'indiv_attachment'
	fields= '__all__'
	
	def get_success_url(self): 
		return '__all__'
		
	def get_context_data(self, **kwargs):
	    context= super(AttachmentDetail, self).get_context_data(**kwargs)
	    context['all_objects']= Attachment.objects.all()
	    
	    return context
	
#Edit each		
class TaskListEdit(UpdateView):
	model= List
	template_name= 'todo/editlist.html'
	context_object_name= 'edit_list'
	fields= '__all__'
	
	def get_success_url(self): 
		return reverse('todo:tasklist', kwargs={'pk': self.object.pk})
        
	def get_context_data(self, **kwargs):
		context= super(TaskListEdit, self).get_context_data(**kwargs)
		context['all_objects']= List.objects.all()  

		return context        
	
class TaskEdit(UpdateView):
	model= Task
	template_name= 'todo/edittask.html'
	context_object_name= 'edit_task'
	fields= '__all__'
	
	def get_success_url(self): 
		return reverse('todo:task', kwargs={'pk': self.object.pk})
        
	def get_context_data(self, **kwargs):
		context= super(TaskEdit, self).get_context_data(**kwargs)
		context['all_objects']= Task.objects.all() 

		return context        
	
class AttachmentEdit(UpdateView):
	model= Attachment
	template_name= 'todo/editattachment.html'
	context_object_name= 'edit_attachment'
	fields= '__all__'
	
	def get_success_url(self):
		return reverse('todo:attachment', kwargs={'pk': self.object.pk})
		
	def get_context_data(self, **kwargs):
		context= super(AttachmentEdit, self).get_context_data(**kwargs)
		context['all_objects']= Attachment.objects.all()
        
		return context        
		
#Delete each		
class TaskListDelete(DeleteView):
	model= List
	template_name= 'todo/deletelist.html'
	context_object_name= 'edit_list'
	success_url= reverse_lazy('todo:tasklists')
	fields= '__all__'
	
	def get_absolute_url(self):
		return reverse_lazy('todo/tasklists')
        
	def get_context_data(self, **kwargs):
		context= super(TaskListDelete, self).get_context_data(**kwargs)
		context['all_objects']= List.objects.all()    
        
		return context
	
class TaskDelete(DeleteView):
	model= Task
	template_name= 'todo/deletetask.html'
	context_object_name= 'edit_task'
	success_url= reverse_lazy('todo:tasks')
	fields= '__all__'
	
	def get_absolute_url(self):
		return reverse_lazy('todo/tasks')
        
	def get_context_data(self, **kwargs):
		context= super(TaskDelete, self).get_context_data(**kwargs)
		context['all_objects']= Task.objects.all()    

		return context
        
class AttachmentDelete(DeleteView):
	model= Attachment
	template_name= 'todo/deleteattachment.html'
	context_object_name= 'delete_attachment'
	success_url= reverse_lazy('todo:attachments')
	fields= '__all__'
	
	def get_absolute_url(self):
		return reverse_lazy('todo/attachments')

	def get_context_data(self, **kwargs):
		context= super(AttachmentDelete, self).get_context_data(**kwargs)
		context['all_objects']= Attachment.objects.all()

		return context

# Create your views here
def tasks(request):
    messages.success(request, ('Task has been added to your List successfully!'))
    return render(request, 'todo/tasks.html', {
            "form": form, "todo": todo, "time": time,
    }) #reloading the page
    		  
def settings(request):	
    return render(request, 'todo/settings.html', {})	

def about(request):	
    return render(request, 'todo/about.html', {})	

def contact(request):	
    my_name= "Maricla Martelli Kandzorra"	
    return render(request, 'todo/contact.html', {
        'name': my_name
    })