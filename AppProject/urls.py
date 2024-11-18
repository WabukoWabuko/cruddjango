from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Index, name="index_page"),
    # path('', views.Create, name="index_page"), 
    # path('update/<int:pk>/', views.Update, name="index_page"), 
    path('<int:pk>', views.Delete, name="index_page")
]