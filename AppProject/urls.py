# from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.list, name='list_page'),
    path('add/', views.add, name='add_page'),
    path('edit/<int:person_id>/', views.edit, name='edit_page'),
    path('delete/<int:person_id>/', views.delete, name='delete_page'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)