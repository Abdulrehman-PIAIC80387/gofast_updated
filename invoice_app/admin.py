from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['sale_number']
   form = InvoiceForm
   list_filter = ['sale_number']
   search_fields = ['sale_number']


class ExpenseAdmin(admin.ModelAdmin):
   list_display = ['expense_number']
   form = ExpenseForm
   list_filter = ['expense_number']
   search_fields = ['expense_number']


class ServiceAdmin(admin.ModelAdmin):
   list_display = ['service_number']
   form = ServiceForm
   list_filter = ['service_number']
   search_fields = ['service_number']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Services,ServiceAdmin)
admin.site.register(Expense,ExpenseAdmin)
