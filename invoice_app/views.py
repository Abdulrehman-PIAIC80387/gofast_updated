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
from json import dumps

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
	
	sale_price_monthly = Invoice.objects.filter(date__month=this_month).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	profit_monthly = Invoice.objects.filter(date__month=this_month).aggregate(Sum("profit"))['profit__sum'] or 0.00
	expense_monthly = Expense.objects.filter(date__month=this_month).aggregate(Sum("amount"))['amount__sum'] or 0.00
	sale_price_yearly = Invoice.objects.filter(date__year=this_year).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	profit_yearly = Invoice.objects.filter(date__year=this_year).aggregate(Sum("profit"))['profit__sum'] or 0.00
	expense_yearly = Expense.objects.filter(date__year=this_year).aggregate(Sum("amount"))['amount__sum'] or 0.00
	current_week = date.today().isocalendar()[1] 
	
	week = Invoice.objects.filter(date__week=current_week)
	
	
	list_date=[1,2,3,4,5,6,7,8,9,10,11,12]
	jan = Invoice.objects.filter(date__month=list_date[0]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	feb = Invoice.objects.filter(date__month=list_date[1]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	march = Invoice.objects.filter(date__month=list_date[2]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	april = Invoice.objects.filter(date__month=list_date[3]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	may = Invoice.objects.filter(date__month=list_date[4]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	june = Invoice.objects.filter(date__month=list_date[5]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	july = Invoice.objects.filter(date__month=list_date[6]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	august = Invoice.objects.filter(date__month=list_date[7]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	sep = Invoice.objects.filter(date__month=list_date[8]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	oct = Invoice.objects.filter(date__month=list_date[9]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	nov = Invoice.objects.filter(date__month=list_date[10]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	dec = Invoice.objects.filter(date__month=list_date[11]).aggregate(Sum("sale_price"))['sale_price__sum'] or 0.00
	last_4 = Invoice.objects.all().order_by('custumer_name')[:4]
	last_4_expense = Expense.objects.all().order_by('expense_name')[:4]
	
	

	

	
	context = {
		
		"sale_price_monthly": sale_price_monthly,
		"profit_monthly":profit_monthly,
		"expense_monthly":expense_monthly,
		"sale_price_yearly":sale_price_yearly,	
		"profit_yearly":profit_yearly,
		"expense_yearly":expense_yearly,
		"week":week,
		
		"jan":jan,
		"feb":feb,
		"march":march,
		"april":april,
		"may":may,
		"june":june,
		"july":july,
		"august":august,
		"sep":sep,
		"nov":nov,
		"oct":oct,
		"dec":dec,
		"last_4":last_4,
		"last_4_expense":last_4_expense,


		
	}
	
	return render(request, "index.html",context)


def add_invoice(request):
	print("----------------------in invoice")
	
	form = InvoiceForm(request.POST)
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
		queryset = Invoice.objects.filter(purchase__icontains=form['purchase'].value(),)

										
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
	print("-------------------in start")
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
			
			startdate = request.POST.get('startdate', None)
			enddate = request.POST.get('enddate', None)
			
			queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')
			
            
											
			context = {
			"form": form,
			"title": title,
			"queryset": queryset,
		}
			return render(request, "salescreen.html", context)  
		if 'btnform2' in request.POST:
			
			startdate = request.POST.get('startdate', None)
			enddate = request.POST.get('enddate', None)
			
			queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')
			pending = Invoice.objects.all().aggregate(Sum('pending'))['pending__sum'] or 0.00
			profit = Invoice.objects.all().aggregate(Sum('profit'))['profit__sum'] or 0.00
			queryset_profit = Invoice.objects.raw('select profit from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')
			profit_date_wise=queryset_profit.aggregate(total=Sum('profit'))
			print("----------------------------------")
			print(profit_date_wise)
            
											
			context = {
			"form": form,
			"title": title,
			"queryset": queryset,
			"profit":profit,
			"pending":pending
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
	print("---------------------in invoice")
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
		queryset = Services.objects.filter(service_name__icontains=form['service_name'].value(),)

										
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
		queryset = Expense.objects.filter(expense_name__icontains=form['expense_name'].value(),)

										
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
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('home')
			

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
		purchase_price = Invoice.objects.all().aggregate(Sum('purchase_price'))['purchase_price__sum'] or 0.00
		sale_price = Invoice.objects.all().aggregate(Sum('sale_price'))['sale_price__sum'] or 0.00
		context = {
		"purchase_price":purchase_price,
		"sale_price":sale_price,
		"queryset": queryset,
		"pending":pending,
		"profit":profit
		
	}

		pdf = render_to_pdf('pdf_template.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

			
		

		    
class ViewPDF_print(View):

    
	def get(self, request, pk ,*args, **kwargs):

		queryset = Invoice.objects.get(id=pk)
		
		context = {"queryset": queryset, 
		
		}
		pdf = render_to_pdf_separate('separate.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
		



def list_invoice_search(request):
	print("-------------------in start")
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	form = InvoiceSearchFormAlloptions(request.POST or None)
	
	context = {
		"title": title,
		"queryset": queryset,
		"form":form
		
	}

	if 'selected' in request.POST:
		
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		sale_number = request.POST.get('sale_number', None)
		purchase = request.POST.get('purchase', None)
		
		queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')
		get = Invoice.objects.all()
		queryset_profit = get.filter(
                
                date__range=[startdate, enddate]
            )
		print(queryset_profit.count)
		queryset_pending = get.filter(
                
                date__range=[startdate, enddate]
            )
		queryset_sales = get.filter(
                
                date__range=[startdate, enddate]
            )
		queryset_purchase = get.filter(
                
                date__range=[startdate, enddate]
            )
    
		profit_date_wise=queryset_profit.aggregate(Sum('profit'))['profit__sum'] or 0.00
		print("----------------------------------")
		print(profit_date_wise)
		pending_date_wise=queryset_pending.aggregate(Sum('pending'))['pending__sum'] or 0.00
		print("----------------------------------")
		print(pending_date_wise)
		sale_date_wise=queryset_sales.aggregate(Sum('sale_price'))['sale_price__sum'] or 0.00
		print("----------------------------------")
		print(sale_date_wise)
		purchase_date_wise=queryset_purchase.aggregate(Sum('purchase_price'))['purchase_price__sum'] or 0.00
		print("----------------------------------")
		print(purchase_date_wise)
		
		pending = Invoice.objects.all().aggregate(Sum('pending'))['pending__sum'] or 0.00
		profit = Invoice.objects.all().aggregate(Sum('profit'))['profit__sum'] or 0.00
		purchase_price = Invoice.objects.all().aggregate(Sum('purchase_price'))['purchase_price__sum'] or 0.00
		sale_price = Invoice.objects.all().aggregate(Sum('sale_price'))['sale_price__sum'] or 0.00
		queryset2 = Invoice.objects.filter(sale_number__icontains=form['sale_number'].value(),
									purchase__icontains=form['purchase'].value()
									)
        
										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
		"pending":pending,
		"profit":profit,
		"purchase_price":purchase_price,
		"sale_price":sale_price,
		"queryset2":queryset2,
	}
		pdf = render_to_pdf_selected('pdf_template.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
	if 'Filter' in request.POST:
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		sale_number = request.POST.get('sale_number', None)
		purchase = request.POST.get('purchase', None)
		custumer_name = request.POST.get('custumer_name', None)
		date = request.POST.get('date', None)
		queryset = Invoice.objects.raw('select * from invoice_app_invoice where date between "'+startdate+'" and "'+enddate+'"')

		queryset2 = Invoice.objects.filter(sale_number__icontains=form['sale_number'].value(),
									purchase__icontains=form['purchase'].value(),custumer_name__icontains=form['custumer_name'].value(),date__icontains=form['date'].value()
									)							
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
		"queryset2":queryset2,

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
		
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		
		queryset = Expense.objects.raw('select * from invoice_app_expense where date between "'+startdate+'" and "'+enddate+'"')

										
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
	}
		pdf = render_to_pdf_selected('expense_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
	if 'Filter' in request.POST:
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		
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
		
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		

		pending = Invoice.objects.all().aggregate(Sum('pending'))['pending__sum'] or 0.00
		profit = Invoice.objects.all().aggregate(Sum('profit'))['profit__sum'] or 0.00
		
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
		"pending":pending,
		"profit":profit,
	}
		pdf = render_to_pdf_selected('travel_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')
	if 'Filter' in request.POST:
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		
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
	received1 = intpending
	
	queryset = Invoice.objects.get(id=pk)
	date_previous = queryset.travel_date
	get_pending = queryset.pending
	received_new = queryset.received
	

    

	if queryset.received1 is 0:
		queryset = Invoice.objects.get(id=pk)
		queryset.received1 = intpending
		queryset.save()
		queryset2 = Invoice.objects.get(id=pk)
		queryset2.date1 = startdate
		queryset2.save()
	elif queryset.received2 is 0:
		queryset = Invoice.objects.get(id=pk)
		queryset.received2 = intpending
		queryset.save()
		queryset2 = Invoice.objects.get(id=pk)
		queryset2.date2 = startdate
		queryset2.save()

	else:
		queryset = Invoice.objects.get(id=pk)
		queryset.received3 = intpending
		queryset.save()
		queryset2 = Invoice.objects.get(id=pk)
		queryset2.date3 = startdate
		queryset2.save()

	remaining = get_pending - intpending
	if queryset.pending <= 0 or remaining < queryset.pending :
		messages.success(request, 'Pending will not Negative')
		return redirect('/list_invoice_ledger')
	else:
		
		updated_received = received_new + intpending
		queryset = Invoice.objects.get(id=pk)
		queryset.pending = remaining
		queryset.save()

	

	




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
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		
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
		
		startdate = request.POST.get('startdate', None)
		enddate = request.POST.get('enddate', None)
		custumer_name1 = request.POST.get('custumer_name')
		
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
		

		
		pending = Invoice.objects.all().aggregate(Sum('pending'))['pending__sum'] or 0.00
		profit = Invoice.objects.all().aggregate(Sum('profit'))['profit__sum'] or 0.00
		context = {
		
		"queryset": queryset,
		"profit":profit,
		"pending":pending,

	}

		pdf = render_to_pdf('ledger_report.html', context)
		return HttpResponse(pdf, content_type='application/pdf')

def ViewPDF_print_leger_separte(request, pk):
	queryset =Invoice.objects.get(id=pk)
	context = {"queryset":queryset }
	pdf = render_to_pdf_separate('ledger_separate.html', context)
	if queryset.received1 != 0:
		print("------------In Received1")
	
		queryset1 =Invoice.objects.get(id=pk)
		
		context = {"queryset1": queryset1,"queryset":queryset }
		pdf = render_to_pdf_separate('ledger_separate.html', context)
		print("below pdf")
		
	if queryset.received2 != 0:
		print("------------In Received2")
		queryset2 =Invoice.objects.get(id=pk)
		
		context = {"queryset2": queryset2,"queryset": queryset, }
		pdf = render_to_pdf_separate('ledger_separate.html', context)
		
	if queryset.received3 != 0:
		print("------------In Received2")
		queryset3 =Invoice.objects.get(id=pk)
		
		context = {"queryset3": queryset3,"queryset": queryset, }
		pdf = render_to_pdf_separate('ledger_separate.html', context)
		
	



	
	return HttpResponse(pdf, content_type='application/pdf')

from datetime import datetime


def list_dashboard(request):
	this_month = datetime.now().month
	
	queryset = Invoice.objects.filter(date__month=this_month).aggregate(Sum("sale_price"))
	
	
	context = {
		
		"queryset": queryset,
		
	}

	
	return render(request, "index.html", context) 

def footer_dashboard(request):
	
	last_4 = Invoice.objects.all().order_by('sales_name')[:4]
	
	rupeya =150
	context = {
		
		"rupeya":rupeya,


		
	}
	dataJSON = dumps(context)
	return (request, "index.html",context)