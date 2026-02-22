from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('blocks/', views.blocks, name='blocks'),
    path('classrooms/', views.classrooms, name='classrooms'),
    path('courses/', views.courses, name='courses'),
    
]