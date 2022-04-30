from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter_forum/', views.enter_forum, name='enter_forum'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('success/', views.success_forum, name = 'success_forum'),
    path('<str:room_name>/', views.room, name='room'),
]