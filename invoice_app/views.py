from django.db.models import query
from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required



from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


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
		queryset = Invoice.objects.filter(sale_number__icontains=form['sale_number'].value(),)

										
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




def list_invoice_search(request):
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = listHistorySearchForm(request.POST or None)
	form2= listHistoryprintForm(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form,
		"form2":form2
	}

	if request.method == 'POST':
		
		if 'btnform1' in request.POST:
			print("---------------------helloo in button1")
			startdate = request.POST.get('startdate', None)
			enddate = request.POST.get('enddate', None)
			print(startdate)
			print(enddate)
			queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')

											
			context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}
			return render(request, "salescreen.html", context)  
		if 'btnform2' in request.POST:
			print("---------------------helloo in btnform2")
			startdate = request.POST.get('startdate', None)
			enddate = request.POST.get('enddate', None)
			print(startdate)
			print(enddate)
			queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')

											
			context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}
			pdf = render_to_pdf_selected('pdf_template.html', context)
			return HttpResponse(pdf, content_type='application/pdf')
			
	

	

	
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


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def render_to_pdf_selected(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def render_to_pdf_separate(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def render_to_pdf_separate1(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#Opens up page as PDF
class ViewPDF(View):

	def get(self, request, *args, **kwargs):
		queryset = Invoice.objects.all()
		context = {
		
		"queryset": queryset,
		
	}

		pdf = render_to_pdf('pdf_template.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

			
		

		    
class ViewPDF_print(View):

    
	def get(self, request, pk ,*args, **kwargs):

		queryset = Invoice.objects.get(id=pk)
		context = {"queryset": queryset, }
		pdf = render_to_pdf_separate('separate.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
		



def list_invoice_search(request):
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = listHistorySearchForm(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if request.method == 'POST':
		
		print("---------------------helloo")
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		print(startdate)
		print(enddate)
		queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')

										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
		pdf = render_to_pdf_selected('pdf_template.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
	return render(request, "salescreen.html", context)  

def list_expense_search(request):
	title = 'List of Invoices'
	queryset = Expense.objects.all()
	form = listHistorySearchFormexpense(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if request.method == 'POST':
		
		print("---------------------helloo")
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		print(startdate)
		print(enddate)
		queryset = Expense.objects.raw('select * from invoice_app_expense where date between "'+startdate+'" and "'+enddate+'"')

										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
		pdf = render_to_pdf_selected('expense_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
	return render(request, "expense_data.html", context) 

class ViewPDF_print_expense(View):

	def get(self, request, *args, **kwargs):
		queryset = Expense.objects.all()
		context = {
		
		"queryset": queryset,
		
	}

		pdf = render_to_pdf('expense_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

		

def ViewPDF_print_expense_aleda(request, pk):
	queryset = Expense.objects.get(id=pk)
	context = {"queryset": queryset, }
	pdf = render_to_pdf_separate('separate_expense.html', context)
	return HttpResponse(pdf, content_type='application/pdf')


def list_Travel_search(request):
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = listHistorytravel(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if request.method == 'POST':
		
		print("---------------------helloo")
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		print(custumer_name1)
		print("---------------------helloo")


		print(startdate)
		print(enddate)
		queryset = Invoice.objects.filter(
	custumer_name__icontains=custumer_name1,
	date__range=[
							startdate,enddate
						]
	)
										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
		pdf = render_to_pdf_selected('travel_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
	return render(request, "travel_data.html", context) 


class ViewPDF_print_travel(View):

	def get(self, request, *args, **kwargs):
		queryset = Invoice.objects.all()
		context = {
		
		"queryset": queryset,
		
	}

		pdf = render_to_pdf('travel_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')	


def ViewPDF_print_Travel_aleda(request, pk):
	queryset =Invoice.objects.get(id=pk)
	context = {"queryset": queryset, }
	pdf = render_to_pdf_separate('travel_separate.html', context)
	return HttpResponse(pdf, content_type='application/pdf')