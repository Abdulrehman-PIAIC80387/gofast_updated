from django.contrib import admin
from .models import Expense, Invoice, services
from .forms import ExpenseForm, InvoiceForm
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['invoice_number']
   form = InvoiceForm
   list_filter = ['invoice_number']
   search_fields = ['invoice_number']


class ExpenseAdmin(admin.ModelAdmin):
   list_display = ['expense_number']
   form = ExpenseForm
   list_filter = ['expense_number']
   search_fields = ['expense_number']


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(services)
admin.site.register(Expense,ExpenseAdmin)
