from django.shortcuts import render
from .forms import InvoiceForm,InvoiceSearchForm,InvoiceUpdateForm,services_form
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


def services_page(request):
	form = services_form(request.POST or None)
	data = services.objects.all()
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/add_services')
	context = {
		"form": form,
		"title": "Services details",
		"data" : data,

	}
	return render(request, "buttons.html",context)

def services_search(request):
	return render(request, "cards.html")


def delete_service(request, pk):
	queryset = services.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/delete_invoice')
	return render(request, 'buttons.html')