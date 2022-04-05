from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls', namespace='todo')),
    path('accounts/', include('django.contrib.auth.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)