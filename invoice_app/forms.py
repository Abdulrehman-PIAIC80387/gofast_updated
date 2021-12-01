from django import forms
from .models import *

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['service_name', 'purchase','purchase_price', 'sale_price',
				'profit', 'Destination', 'received',
				'pending','sale_number','custumer_name','phone'
				]
	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('sale_number')
		if not invoice_number:
			raise forms.ValidationError('This field is required')
			return invoice_number
		    


class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['sale_number']


class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['service_name', 'purchase','purchase_price', 'sale_price',
				'profit', 'Destination', 'received',
				'pending','sale_number','custumer_name','phone'
				]






class ServiceForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['service_number','service_name','remarks'
				]
	def clean_Expense_number(self):
		expense_number = self.cleaned_data.get('expense_number')
		if not expense_number:
			raise forms.ValidationError('This field is required')


class ServiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['service_number','service_name','remarks'
		
				]


class serviceSearchForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['service_number']



class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['expense_number','amount','expense_name'
				]
	def clean_Expense_number(self):
		expense_number = self.cleaned_data.get('expense_number')
		if not expense_number:
			raise forms.ValidationError('This field is required')


class ExpenseUpdateForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['expense_number','amount','expense_name'
				]

class ExpenseSearchForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['expense_number']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']