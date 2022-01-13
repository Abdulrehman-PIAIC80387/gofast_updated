from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['purchase']
   form = InvoiceForm
   list_filter = ['purchase']
   search_fields = ['purchase']


class ExpenseAdmin(admin.ModelAdmin):
   list_display = ['expense_name']
   form = ExpenseForm
   list_filter = ['expense_name']
   search_fields = ['expense_name']


class ServiceAdmin(admin.ModelAdmin):
   list_display = ['service_name']
   form = ServiceForm
   list_filter = ['service_name']
   search_fields = ['service_name']

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Services,ServiceAdmin)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(New)
