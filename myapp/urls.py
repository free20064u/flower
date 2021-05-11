from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('flower/<slug:slug>/', views.detail, name='detail'),
    path('tags/<slug:slug>/', views.tags, name='tags'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
] 


