from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.Booking, name='booking'),
    path('doctors/', views.Doctors, name='doctors'),
    path('contact/', views.Contact, name='contact'),
    path('department/', views.departmnet, name='dept'),
    path('reg/', views.register, name='reg'),
    path('login/', views.login, name='login'),

]