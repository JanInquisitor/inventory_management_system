from django.contrib import admin
from storages.models import Product, Storage, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = [('name')]
    search_fields = [('name',)]


class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'upc', 'quantity', 'date', 'storage')
    list_filter = ('tags', 'storage')
    search_fields = ('name', 'tags', 'storage')


admin.site.register(Product, ProductAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Company, CompanyAdmin)
