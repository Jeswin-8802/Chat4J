from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('success/', views.success, name = 'success'),
    path('upload/', views.upload, name = 'upload'),
]