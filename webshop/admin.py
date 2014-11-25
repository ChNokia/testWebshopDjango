# -*- coding: utf-8 -*-

from django.contrib import admin
from webshop.models import (
							Category,
							Customer,
							Product,
							ProductImages
							)

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

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#class CustomerAdmin(UserAdmin):
#	list_display = ('username', 'email', 'date_created')
	#list_editable = ('email')
#	search_fields = ['username', 'email']

#	fieldsets = (
 #       (None, {'fields': ('username', 'password')}),
  #      (('Personal info'), {'fields': (
   #             'first_name', 'last_name', 'email'
    #        )}),
     #   (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
      #  (('Important dates'), {'fields': ('last_login', 'date_joined')}),
       # (('Groups'), {'fields': ('groups',)}),
    #)
class CustomerInline(admin.StackedInline):
	model = Customer
	can_delete = False
	verbose_name_plural = 'profile'

class CustomerAdmin(UserAdmin):
	inlines = (CustomerInline, )

admin.site.unregister(User)
admin.site.register(User, CustomerAdmin)

#admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
#admin.site.register(Customer, CustomerAdmin)

