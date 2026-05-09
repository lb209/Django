from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_student, name='read'),
    path('create/', views.create_student, name='create'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),

   
]