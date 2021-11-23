from django.contrib import admin
from .models import Invoice, services
from .forms import InvoiceForm
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['invoice_number']
   form = InvoiceForm
   list_filter = ['invoice_number']
   search_fields = ['invoice_number']
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(services)