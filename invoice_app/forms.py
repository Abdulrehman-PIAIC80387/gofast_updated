from django import forms
from .models import Expense, Invoice, services

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['service_name', 'purchase','purchase_price', 'sale_price',
				'profit', 'Destination', 'received',
				'pending','invoice_number','custumer_name','phone'
				]
	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError('This field is required')
			return invoice_number
		    


class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['invoice_number']


class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['service_name', 'purchase','purchase_price', 'sale_price',
				'profit', 'Destination', 'received',
				'pending','invoice_number','custumer_name','phone'
				]

class services_form(forms.ModelForm):
	class Meta:
		model = services
		fields = ['service_name']



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