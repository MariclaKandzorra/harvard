from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from django.urls import path, include, reverse, reverse_lazy, Resolver404, resolve, NoReverseMatch

from todo.models import List, Task, Attachment


class StaticSitemap(Sitemap):    
    def items(self):
        return ['todo:contact', 'todo:about', 'todo:settings',]

    def location(self, item):
        return reverse(item)
        
class TaskListViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'
    limit=1000
    
    def items(self):
        return List.objects.all()

    def location(self, item):
        return reverse('todo:tasklist', args=[item.id])
        
    def lastmod(self, item):
        return item.updated_at  

class TaskViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'
    limit=1000

    def items(self):
        return Task.objects.filter(completed=False)

    def lastmod(self, item):
        return item.updated_at       
        
    def location(self, item):
        return reverse('todo:task', args=[item.id])    
        
class AttachmentViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'
    limit=1000

    def items(self):
        return Attachment.objects.all()

    def lastmod(self, item):
        return item.timestamp       
        
    def location(self, item):
        return reverse('todo:attachment', args=[item.pk])            
