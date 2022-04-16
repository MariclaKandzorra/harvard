import datetime
import os
import textwrap

from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.auth.models import User
from django.db import DEFAULT_DB_ALIAS, models
from django.db.transaction import Atomic, get_connection
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from datetime import datetime, timedelta


def get_attachment_upload_dir(instance, filename):
    return "/".join(["tasks", "attachment", str(instance.task.id), filename])
 		    
class LockedAtomicTransaction(Atomic):
	
	def __init__(self, *models, using=None, savepoint=None):
		if using is None:
			using= Default_DB_Alias
		super().__init__(using, savepoint)
		self.models= models
		
	def __enter__(self):
		super(LockedAtomicTransaction, self).__enter__()
		
		if settings.DATABASE[self.using]["Engine"] != "django.db.backends.sqlite3":
			cursor=None
			try:
				cursor= get.connection(self.using).cursor()
				for model in self.models:
					cursor.execute("LOCK TABLE {table_name}".format(table_name=model._meta.db_table))
			finally:
				if cursor and not cursor.closed:
					cursor.close()

# Create your models for the admin area here.
# New Database class Todo-"List" and add new todo-task to list
class List(models.Model):  
    name= models.CharField(max_length=900) #add new todo to list, varchar
    created_by= models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    assigned_to= models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name= "todo_list_assigned_to", on_delete=models.CASCADE,)
    slug= models.SlugField(max_length=5)
    note= models.TextField()
    completed= models.BooleanField(default= False) #checkbox
    # Maps to create_date table column.
    date= models.DateTimeField(default=datetime.now, blank=True, null= True)
    updated_at= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
    	return self.name + ' | | Completed: ' + str(self.completed) + ' | | ListID: ' + str(self.id) + '| | Assigned to:' + str(self.assigned_to)
    	
    def get_absolute_url(self):
    	self.model.__name__
    	return reverse('tasklist', args={"list_id": str(self.id)})
    	
    class Meta:
    	ordering=["name", "assigned_to", "date"]
    	verbose_name_plural="Task Lists"
    	unique_together= ("created_by", "slug")
    	unique_together= ("assigned_to", "slug")
    	
 		
class Task(models.Model):
    STATUS= [
    ('TODO', 'TODO'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('PAUSE', 'PAUSE'),
    ('DONE', 'DONE'),
    ]
    
    PRIORITY= [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    ]
 		
    task_list= models.ForeignKey(List, on_delete= models.CASCADE, null=True)
    created_by= models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name="todo_created_by", on_delete=models.CASCADE,)
    assigned_to= models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name="todo_task_assigned_to", on_delete=models.CASCADE,)
    title= models.CharField(max_length=900) #add new todo to list, varchar
    slug= models.SlugField(max_length=5)
    note= models.TextField(blank= True, null= True)
    priority= models.IntegerField(choices= PRIORITY)
    status= models.CharField(max_length= 15, choices=STATUS)
    # Maps to create_date table column.
    created_date= models.DateTimeField(default=datetime.now, blank=True, null= True)
    updated_at= models.DateTimeField(auto_now=True, null=True)
    due_date= models.DateField(default=datetime.now()+timedelta(days=15), blank=True, null=True)
    completed= models.BooleanField(default= False) #checkbox
    
    def get_absolute_url(self):
        self.model.__name__
        return reverse('task', args={"task_id": str(self.id)})
    
    def overdue_status(self):
        "Returns wether the Task's due date has passed or not."
        if self.due_date and datetime.today() > self.due_date:
            return True
            
    def __str__(self):
        return self.title  + ' | | from Task List: ' + self.task_list.name
 		
    def save(self, **kwargs):
        if self.completed:
            self.completed_date= datetime.now()
        super(Task,self).save()
        
    def merge_into(self, merge_target):
        if merge_target.pk == self.pk:
            raise ValueError("can't merge a task with self")
            
        with LockedAtomicTransaction(Attachement):
            Attachement.objects.filters(task.self).update(task=merge_target)
            self.delete()
 	
    class Meta:
        ordering= ["task_list", "title", "due_date", "priority", "status"]
       
        
class Attachment(models.Model):
    task= models.ForeignKey(Task, on_delete= models.CASCADE, null= True)
    file_name= models.CharField(max_length=900, blank=True, null=True) 
    added_by= models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name="todo_added_by",  on_delete=models.CASCADE,)
    timestamp= models.DateTimeField(default=datetime.now, blank=True, null=True)
    note= models.TextField(blank= True, null= True)
    file= models.FileField(upload_to= 'media/', max_length=855)
 		
    def get_absolute_url(self):
        self.model.__name__
        return reverse('attachment', args={"attachment_id": str(self.id)})
 		
    def filename(self):
        return os.path.basename(str(self.file_name))
 			
    def extension(self):
        name, extension= os.path.splitext(str(self.file.name))
        return extension
 			
    def __str__(self):
        return f"{self.task.title} - from: {self.task.task_list.name} - {self.file_name}"
 			
    def get_attachment_upload_dir(instance, file_name):
        return "/".join(["tasks", "attachment", str(instance.task.id), file_name])
    
    class Meta:
        ordering= ["task", "timestamp"]