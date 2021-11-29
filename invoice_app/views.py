from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
	
	
	return render(request, "index.html")


def add_invoice(request):
	form = InvoiceForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/list_invoice')
	context = {
		"form": form,
		"title": "New Invoice",
	}
	return render(request, "entry.html", context)

		
    



def list_invoice(request):
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = InvoiceSearchForm(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if request.method == 'POST':
		queryset = Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value(),)

										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_invoice.html", context)    
	
def update_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	form = InvoiceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InvoiceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_invoice')

	context = {
		'form':form
	}
	return render(request, 'entry.html', context)


def delete_invoice(request, pk):
	queryset = Invoice.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_invoice')
	return render(request, 'delete_invoice.html')




def add_service(request):
	queryset = Services.objects.all()
	form = ServiceForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/add_service')
	context = {
		"form": form,
		"title": "New Service",
		"queryset": queryset,
	}
	return render(request, "buttons.html", context)


def list_services(request):
	title = 'List of Services'
	queryset = Services.objects.all()
	form = serviceSearchForm(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if request.method == 'POST':
		queryset = ServiceForm.objects.filter(service_number__icontains=form['service_number'].value(),)

										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
	return render(request, "cards.html", context)

def update_Service(request, pk):
	queryset = Services.objects.get(id=pk)
	form = ServiceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ServiceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/add_service')

	context = {
		'form':form
	}
	return render(request, 'buttons.html', context)


def delete_service(request, pk):
	queryset = Services.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/add_service')
	return render(request, 'delete_invoice.html')


def add_expense(request):
	form = ExpenseForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/list_expense')
	context = {
		"form": form,
		"title": "New Expense",
	}
	return render(request, "utilities-color.html", context)




def list_expense(request):
	title = 'List of Invoices'
	queryset = Expense.objects.all()
	form = ExpenseSearchForm(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if request.method == 'POST':
		queryset = Expense.objects.filter(expense_number__icontains=form['expense_number'].value(),)

										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
	return render(request, "utilities-other.html", context)    


def update_Expense(request, pk):
	queryset = Expense.objects.get(id=pk)
	form = ExpenseUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ExpenseUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_expense')

	context = {
		'form':form
	}
	return render(request, 'utilities-color.html', context)


def delete_Expense(request, pk):
	queryset = Expense.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_expense')
	return render(request, 'delete_invoice.html')

