from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('about/', TemplateView.as_view(template_name='about.html'),
                      name='about'),
     path('contact/', TemplateView.as_view(template_name='contact.html'),
                      name='contact'),
     path('<slug:slug>/', views.post_detail, name='post_detail'),
   path('summernote/',include('django_summernote.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)