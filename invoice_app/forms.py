from django import forms
from .models import *
from django.forms.widgets import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class DateInput(forms.DateInput):
    input_type = 'date'
"""
class RadioSelect(forms.DateInput):
   choices=[
            (True, 'yes'),
            (False, 'no')             
        ]
"""

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['service_name', 'purchase','purchase_price', 'sale_price',
				'profit', 'Destination', 'received',
				'pending','sale_number','custumer_name','phone','date','remarks','date_time','manual_issue_date'
				]
		widgets = {
            'manual_issue_date': DateInput(),
			 'date_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
	
		    
class listHistorySearchForm(forms.ModelForm):
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = Invoice
		fields = ['start_date', 'end_date']

class listHistoryprintForm(forms.ModelForm):
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = Invoice
		fields = ['start_date', 'end_date']


class list_pdf(forms.ModelForm):
	generate_invoice=forms.BooleanField()
	class Meta:
		model = Invoice
		fields = ['generate_invoice']
		

	

class InvoiceSearchForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['purchase']

class InvoiceSearchFormAlloptions(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['sale_number','date','purchase','custumer_name']
		widgets = {
            'date': DateInput(),
        }


class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['service_name', 'purchase','purchase_price', 'sale_price',
				'profit', 'Destination', 'received',
				'pending','sale_number','custumer_name','phone','date','remarks','date_time','manual_issue_date'
				]
		widgets = {
            'manual_issue_date': DateInput(),
			 'date_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }






class ServiceForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['service_name','remarks'
		
				]
	


class ServiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['service_name','remarks'
		
				]


class serviceSearchForm(forms.ModelForm):
	class Meta:
		model = Services
		fields = ['service_name']



class ExpenseForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['amount','expense_name','remarks_expense','date'
				]
		widgets = {
            'date': DateInput(),
        }
	def clean_Expense_name(self):
		expense_name = self.cleaned_data.get('expense_name')
		if not expense_name:
			raise forms.ValidationError('This field is required')


class ExpenseUpdateForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['amount','expense_name','remarks_expense','date'
				]

class ExpenseSearchForm(forms.ModelForm):
	class Meta:
		model = Expense
		fields = ['expense_name']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class listHistorySearchFormexpense(forms.ModelForm):
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = Expense
		fields = ['start_date', 'end_date']


class listHistorytravel(forms.ModelForm):
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = Invoice
		fields = ['custumer_name', 'start_date', 'end_date']
		widgets = {
            'start_date': DateInput(),
			'end_date': DateInput(),

        }
