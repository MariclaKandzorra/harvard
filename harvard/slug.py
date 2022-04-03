Modules.py

def get_absolute_url(self):
    	self.model.__name__
    	return reverse('todo:tasklist', args={"list_id": str(self.id)})
    	
    	
def get_absolute_url(self):
 		self.model.__name__
 		return reverse('todo:task', args={"task_id": str(self.id)})
 		

def get_absolute_url(self):
 			self.model.__name__
 			return reverse('todo:attachment', args={"attachment_id": str(self.id)})
 			
 			
Tasks.html

<p class="text-md-center fw-bold fs-2 bg-light border"><a href="{% url 'todo:task' pk=task_id %}">{{ task.title }} </a></p>

<p class="text-md-center fw-bold fs-2 bg-light border"><a href="{% url 'todo:task' pk=task_id %}">{{ task.title }} </a></p>


Taskslists.html

<a href="{% url 'todo:tasklist' pk=list_id %}">{{ list.name }} </a>

<a href="{% url 'todo:tasklist' pk=list_id %}">{{ list.name }} </a>


Views.py

    template_name= 'todo/tasklist.html
	slug_url_kwarg= 'str(list.id)'
	slug_field='str(list.id)'
	
	def get_success_url(self):
		return reverse_lazy('todo:tasklist', kwargs=[str(self.id)])	
	
template_name= 'todo/task.html
	slug_url_kwarg= 'str(title.id)'
	slug_field='str(title.id)'
	
	def get_success_url(self):
		return reverse_lazy('todo:task', kwargs=[str(self.id)])
		
template_name= 'todo/attachment.html
	slug_url_kwarg= 'str(attachment.id)'
	slug_field='str(attachment.id)'
	
	def get_success_url(self):
		return reverse_lazy('todo:attachment', kwargs=[str(self.id)])

Urls.py		
		
path('tasklist/<int:pk>', TaskListDetail.as_view(), name= 'tasklist'),
path('task/<int:pk>', TaskDetail.as_view(), name= 'task'),
path('attachment/<int:pk>', AttachmentDetail.as_view(), name= 'attachment'),