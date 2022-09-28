from django.contrib import admin
from .models import Business

# Register your models here.
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['id','product','quality_percentage', 'demand_percent', 'earning', 'expanses', 'unique_products']

