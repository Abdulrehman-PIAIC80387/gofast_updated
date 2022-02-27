from django.db import models
from django.utils import timezone
from django import forms
import datetime
from django.utils.timezone import now
# Create your models here.
class Invoice(models.Model):
    
	service_name = models.ForeignKey('Services',default='', on_delete=models.CASCADE)
	sale_number =  models.CharField('PNR', max_length=120, default='', blank=True, null=True,unique=True)
	custumer_name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	
	purchase = models.CharField('Passenger Name', max_length=120, default='', blank=True, null=True)
	purchase_price = models.IntegerField('Purchase Price', default=0, blank=True, null=True)
	sale_price = models.IntegerField('Sale Price', default=0, blank=True, null=True)
	date = date = models.DateField("Travel Date",null=True)
	remarks = models.CharField('Remarks', max_length=120, default='', blank=True, null=True)
	date = date = models.DateField("Travel Date",null=True,blank=True)
	travel_time= models.TimeField("Travel Time", null=True,blank=True,default=now)
	manual_issue_date = models.DateField("Issue Date",null=True,blank=True)
	purchase1 = models.CharField('Passenger', max_length=120, default='', blank=True, null=True)
	purchase2 = models.CharField('Passenger', max_length=120, default='', blank=True, null=True)
    
	purchase3 = models.CharField('Passenger', max_length=120, default='', blank=True, null=True)
	Destination1 = models.CharField('Destination', max_length=120, default='', blank=True, null=True)
	Destination2 = models.CharField('Destination', max_length=120, default='', blank=True, null=True)
	Destination3 = models.CharField('Destination', max_length=120, default='', blank=True, null=True)
	Travel_date1 = models.DateField("Travel Date",null=True,blank=True)
	Travel_date2 = models.DateField("Travel Date",null=True,blank=True)
	Travel_date3 = models.DateField("Travel Date",null=True,blank=True)
	travel_time1 = models.TimeField("Time Travel", null=True,blank=True,default=now)
	travel_time2 = models.TimeField("Time Travel", null=True,blank=True,default=now)
	travel_time3 = models.TimeField("Time Travel", null=True,blank=True,default=now)
   
	
    

	
	date1 = models.DateField(null=True,blank=True)
	date2 = models.DateField(null=True,blank=True)
	date3 = models.DateField(null=True,blank=True)
	received1 = models.IntegerField('Pending ', default=0, blank=True, null=True)
	received2 = models.IntegerField('Pending ', default=0, blank=True, null=True)
	received3 = models.IntegerField('Pending ', default=0, blank=True, null=True)
		
		
	profit = models.IntegerField('Profit', default=0, blank=True, null=True)
	

	Destination = models.CharField('Destination', max_length=120, default='', blank=True, null=True)
	travel_date = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)
	received = models.IntegerField('Received', default=0, blank=True, null=True)
	pending = models.IntegerField('Pending ', default=0, blank=True, null=True)
	phone = models.IntegerField('Phone number', default='0', blank=True, null=True)
	generate_invoice = models.BooleanField(default=False,blank=False)
    
	
	def __str__(self):
		return self.custumer_name or ''



class Services(models.Model):
	
	service_name = models.CharField('Service name', max_length=120, default='', blank=True, null=True)
	remarks = models.CharField('Remarks', max_length=120, default='', blank=True, null=True)
	def __str__(self):
		return self.service_name or ''



class Expense(models.Model):
    
	expense_name = models.CharField('Expense name', max_length=120, default='', blank=True, null=True)

	amount = models.IntegerField('Expense Amount ', default=0, blank=True, null=True)
	travel_date = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)
	date = date = models.DateField(null=True)
	remarks_expense = models.CharField('Remarks', max_length=120, default='', blank=True, null=True)
	def __str__(self):
		return self.expense_number

class New(models.Model):
	history = models.ForeignKey(Invoice, on_delete=models.CASCADE,related_name="new")
	date1 = models.DateField(null=True,blank=True)
	date2 = models.DateField(null=True,blank=True)
	date3 = models.DateField(null=True,blank=True)
	pending1 = models.IntegerField('Pending ', default=0, blank=True, null=True)
	pending2 = models.IntegerField('Pending ', default=0, blank=True, null=True)
	pending3 = models.IntegerField('Pending ', default=0, blank=True, null=True)





