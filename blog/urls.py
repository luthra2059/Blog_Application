from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
     path('', views.PostList.as_view(), name='home'),
     path('about/', TemplateView.as_view(template_name='about.html'),
                      name='about'),
     path('contact/', TemplateView.as_view(template_name='contact.html'),
                      name='contact'),
     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]