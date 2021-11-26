from django.db import models

# Create your models here.
class Invoice(models.Model):
    
	service_name = models.OneToOneField("services",on_delete=models.CASCADE,default='')
	invoice_number = models.IntegerField(blank=True, null=True)
	custumer_name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	
	purchase = models.CharField('Purchase Name', max_length=120, default='', blank=True, null=True)
	purchase_price = models.IntegerField('Purchase Price', default=0, blank=True, null=True)
	sale_price = models.IntegerField('Sale Price', default=0, blank=True, null=True)
	

	
	profit = models.IntegerField('Profit', default=0, blank=True, null=True)
	

	Destination = models.CharField('Destination', max_length=120, default='', blank=True, null=True)
	travel_date = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)
	received = models.IntegerField('Received', default=0, blank=True, null=True)
	pending = models.IntegerField('Pending ', default=0, blank=True, null=True)
	phone = models.IntegerField('Phone number', default='0', blank=True, null=True)

	
	def __str__(self):
		return self.invoice_number



class services(models.Model):
	auto_increment_id = models.AutoField(primary_key=True)
	service_name = models.CharField('Service name', max_length=120, default='', blank=True, null=True)
	def __str__(self):
		return self.service_name



class Expense(models.Model):
    
	expense_name = models.CharField('Expense name', max_length=120, default='', blank=True, null=True)
	expense_number = models.IntegerField('Expense Number ', default=0, blank=True, null=True)
	amount = models.IntegerField('Expense Amount ', default=0, blank=True, null=True)
	travel_date = models.DateTimeField(auto_now_add=True, auto_now=False,null=True)
	
	def __str__(self):
		return self.expense_number