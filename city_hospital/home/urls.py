from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.Booking, name='booking'),
    path('doctors/', views.Doctors, name='doctors'),
    path('contact/', views.Contact, name='contact'),
    path('department/', views.departmnet, name='dept'),
    path('reg/', views.register, name='reg'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('userbookings/', views.viewBooking, name='userbookings'),
    path('delete/<int:did>', views.deleteBooking, name='delete'),
    path('edit/<int:eid>', views.editBooking, name='editbooking'),


]