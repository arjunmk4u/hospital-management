from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('booking/', views.Booking),
    path('doctors/', views.Doctors),
    path('contact/', views.Contact),
    path('department/', views.departmnet),
]