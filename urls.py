from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('create/', views.create, name='create_page'),  # نام: create_page
    path('delete/<int:id>/', views.delete, name='delete'),
    path('profile/<int:id>/', views.profile, name='profile'),
]