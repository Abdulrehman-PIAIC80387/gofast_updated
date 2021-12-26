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
from django.db.models import Sum


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from datetime import date

# Create your views here.
def home(request):
	this_month = datetime.now().month
	this_year = datetime.now().year
	print(this_year)
	sale_price_monthly = Invoice.objects.filter(date__month=this_month).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	profit_monthly = Invoice.objects.filter(date__month=this_month).aggregate(Sum("profit"))['profit__sum'] or 0.00
	expense_monthly = Expense.objects.filter(date__month=this_month).aggregate(Sum("amount"))['amount__sum'] or 0.00
	sale_price_yearly = Invoice.objects.filter(date__year=this_year).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	profit_yearly = Invoice.objects.filter(date__year=this_year).aggregate(Sum("profit"))['profit__sum'] or 0.00
	expense_yearly = Expense.objects.filter(date__year=this_year).aggregate(Sum("amount"))['amount__sum'] or 0.00
	current_week = date.today().isocalendar()[1] 
	print(current_week)
	week = Invoice.objects.filter(date__week=current_week)
	
	print("---------------- in dashboard")
	print(sale_price_monthly)
	context = {
		
		"sale_price_monthly": sale_price_monthly,
		"profit_monthly":profit_monthly,
		"expense_monthly":expense_monthly,
		"sale_price_yearly":sale_price_yearly,	
		"profit_yearly":profit_yearly,
		"expense_yearly":expense_yearly,
		"week":week,


		
	}
	
	return render(request, "index.html",context)


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
		
		pending = Invoice.objects.all().aggregate(Sum('pending'))['pending__sum'] or 0.00
		profit = Invoice.objects.all().aggregate(Sum('profit'))['profit__sum'] or 0.00
		context = {
		
		"queryset": queryset,
		"pending":pending,
		"profit":profit
		
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

	if 'selected' in request.POST:
		
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
	if 'Filter' in request.POST:
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
		return render(request, "salescreen.html", context) 

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

	if 'selected' in request.POST:
		
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
	if 'Filter' in request.POST:
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
		return render(request, "expense_data.html", context) 

	
	return render(request, "expense_data.html", context) 

class ViewPDF_print_expense(View):

	def get(self, request, *args, **kwargs):
		queryset = Expense.objects.all()
		total_expense = Expense.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0.00
		context = {
		
		"queryset": queryset,
		"total_expense":total_expense,
		
	}

		pdf = render_to_pdf('expense_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

		

def ViewPDF_print_expense_aleda(request, pk):
	print("aleda zindagi")
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

	if 'selected' in request.POST:
		
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
	if 'Filter' in request.POST:
		print("---------------------helloo in filter")
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		print(startdate)
		print(enddate)
		queryset = Invoice.objects.filter(custumer_name__icontains=custumer_name1,date__range=[
							startdate,enddate
						])
											
		context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}
		return render(request, "travel_data.html", context) 
	return render(request, "travel_data.html", context) 


class ViewPDF_print_travel(View):

	def get(self, request, *args, **kwargs):
		queryset = Invoice.objects.all()
		pending = Invoice.objects.all().aggregate(Sum('pending'))['pending__sum'] or 0.00
		profit = Invoice.objects.all().aggregate(Sum('profit'))['profit__sum'] or 0.00
		context = {
		
		"queryset": queryset,
		"pending":pending,
		"profit":profit
	}

		pdf = render_to_pdf('travel_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')	


def ViewPDF_print_Travel_aleda(request, pk):
	queryset =Invoice.objects.get(id=pk)
	context = {"queryset": queryset, }
	pdf = render_to_pdf_separate('travel_separate.html', context)
	return HttpResponse(pdf, content_type='application/pdf')



def update_invoice_ledger(request, pk):
	
	startdate = request.POST.get('startdate', None)
	pending_added = request.POST.get('pending_added', None)
	intpending = int(pending_added)
	print("-------------------------")
	print(startdate)
	print(intpending)
	
	queryset = Invoice.objects.get(id=pk)
	date_previous = queryset.date
	get_pending = queryset.pending
	received_new = queryset.received
	print("-------------dating")
	print(date_previous)
	print(get_pending)

	remaining = get_pending - intpending
	updated_received = received_new + intpending
	queryset = Invoice.objects.get(id=pk)
	queryset.pending = remaining
	queryset.save()

	queryset2 = Invoice.objects.get(id=pk)
	queryset2.date = startdate
	queryset2.save()

	queryset3 = Invoice.objects.get(id=pk)
	queryset3.received = updated_received
	queryset3.save()




	return redirect('/list_invoice_ledger')

def list_invoice_ledger(request):
	
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = InvoiceSearchForm(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
	}

	if 'selected' in request.POST:
		print("---------------------helloo in selected")
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		print(custumer_name1)


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
	

	if 'Filter' in request.POST:
		print("---------------------helloo in filter")
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		print(startdate)
		print(enddate)
		queryset = Invoice.objects.filter(custumer_name__icontains=custumer_name1,date__range=[
							startdate,enddate
						])
											
		context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}
		return render(request, "ledger_data.html", context) 
	return render(request, "ledger_data.html", context) 

class ViewPDF_print_ledger(View):

	def get(self, request, *args, **kwargs):
		queryset = Invoice.objects.all()
		context = {
		
		"queryset": queryset,
		
	}

		pdf = render_to_pdf('ledger_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

def ViewPDF_print_leger_separte(request, pk):
	queryset =Invoice.objects.get(id=pk)
	context = {"queryset": queryset, }
	pdf = render_to_pdf_separate('ledger_separate.html', context)
	return HttpResponse(pdf, content_type='application/pdf')

from datetime import datetime


def list_dashboard(request):
	this_month = datetime.now().month
	
	queryset = Invoice.objects.filter(date__month=this_month).aggregate(Sum("sale_price"))
	print("---------------- in dashboard")
	
	context = {
		
		"queryset": queryset,
		
	}

	
	return render(request, "index.html", context) 

