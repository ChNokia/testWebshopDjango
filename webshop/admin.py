# -*- coding: utf-8 -*-

from django.contrib import admin
from webshop.models import Category, Product, ProductImages

#class CatalogAdmin(admin.ModelAdmin):
#	list_display = ('name', 'publisher', 'put_date')

class ProductImagesInline(admin.StackedInline):
	model = ProductImages
	extra = 1


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display = ('name', 'slug', 'published', 'orderin', 'pic')
	list_editable = ('slug', 'published', 'orderin')

class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}
	list_display = ('name', 'category', 'slug', 'published', 'orderin', 'manufacturer', 'price_in_ua', 'pic')
	list_editable = ('slug', 'published', 'orderin')
	inlines = [ProductImagesInline]
	list_filter = ('category',)
	search_fields = ['name']

#admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)

