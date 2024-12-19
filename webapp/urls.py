
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),
    path('register/', views.register, name="register"),
    path('user-login/', views.login, name="user-login"),
    path('user-logout/', views.logout, name="user-logout"),
    # OTP SET UP
    path('otp-setup/', views.otpSetup, name="otp-setup"), 
    # OTP VERIFICATION
    path('otp-verify/', views.otpVerify, name="otp-verify"),
    # READ MULTIPLE CUSTOMERS
    path('user-dashboard', views.dashboard, name="user-dashboard"),
    # CREATE CUSTOMER
    path('customer-create', views.createCustomer, name="customer-create"),
    # UPDATE CUSTOMER
    path('customer-update/<str:pk>', views.updateCustomer, name="customer-update"),
    # READ SINGLE CUSTOMER
    path('customer-read/<str:pk>', views.readCustomer, name="customer-read"),
    # DELETE CUSTOMER
    path('customer-delete/<str:pk>', views.deleteCustomer, name="customer-delete"),
    # CREATE EMPLOYMENT DETAILS
    path('customer/<int:pk>/employment/create/', views.createEmployment, name='employment-create'),
    # READ EMPLOYMENT DETAILS
    path('customer/<int:pk>/employment/read/', views.readEmployment, name="employment-read"),
    # DELETE EMPLOYMENT DETAILS
    path('employment/<int:pk>/employment/delete/', views.deleteEmployment, name="employment-delete"),
    
] 
