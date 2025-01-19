from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='app'),
    path('register/', views.registerationform, name='registerationform'),
    path('create/', views.createventform, name='createventform'),
    path('details/<int:id>', views.details, name='details'),
    path('tasksform/', views.tasksform, name='tasksform'),
    
]
