"""invoices_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invoice_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('list_invoice/', views.list_invoice, name='list_invoice'),
    path('list_invoice_search/', views.list_invoice_search, name='list_invoice_search'),
    path('add_service/', views.add_service, name='add_service'),
    path('list_services/', views.list_services, name='list_services'),
    #path('list_invoice_print/', views.list_invoice_print, name='list_invoice_print'),
    path('update_Service/<str:pk>/', views.update_Service, name="update_Service"),
    path('delete_service/<str:pk>/', views.delete_service, name="delete_service"),
    path('update_invoice/<str:pk>/', views.update_invoice, name="update_invoice"),
    path('delete_invoice/<str:pk>/', views.delete_invoice, name="delete_invoice"),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('list_expense/', views.list_expense, name='list_expense'),
    path('update_expense/<str:pk>/', views.update_Expense, name="update_expense"),
    path('delete_expense/<str:pk>/', views.delete_Expense, name="delete_expense"),
    path('register/', views.registerPage, name="register"),
	path('', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('ViewPDF_separate/', views.ViewPDF_separate.as_view(), name="ViewPDF_separate"),

]
