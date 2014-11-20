# -*- coding: utf-8 -*-

from django.db import models
import datetime
import random
from django.conf import settings
from django.contrib import auth
#from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_model

def make_upload_path(instance, file_name, prefix = False):
	n1 = random.randint(0, 10000)
	n2 = random.randint(0, 10000)
	n3 = random.randint(0, 10000)
	file_name = '{0}_{1}_{2}.jpg'.format(n1, n2, n3)

	return u'images/%Y/%m/%d/{0}'.format(file_name)
'''
class Catalog(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.SlugField(max_length = 150)
	publisher = models.CharField(max_length = 300)
	description = models.TextField()
	put_date = models.DateTimeField(default = datetime.datetime.now())

	def __unicode__(self):
		return u'%s: %s - %s' % (self.name,
								self.slug,
								self.description)
'''
class Category(models.Model):
	#catalog = models.ForeignKey('Catalog',
								#related_name = 'categories')
	name = models.CharField(max_length = 150, blank = True, verbose_name = "Категорія")
	parent = models.ForeignKey('self', blank = True, null = True,
								related_name = 'children')
	title = models.CharField(max_length = 200, default = "", blank = True,
								verbose_name = "Заголовок")
	meta_desc = models.CharField(max_length = 200, default = "", blank = True,
								verbose_name = "Мета опис")
	meta_key = models.CharField(max_length = 200, default = "", blank = True,
								verbose_name = "Ключові слова")
	slug = models.CharField(max_length = 250, default = "", blank = True,
								verbose_name = "Урл")
	photo = models.ImageField(upload_to = make_upload_path, default = "", blank = True,
							verbose_name = "Зображення")
	published = models.BooleanField(verbose_name = u"Опубліковано") 
	date_add = models.DateTimeField(default = datetime.datetime.now(), auto_now_add = True,
									verbose_name = "Дата створення")
	orderin = models.IntegerField(default = 0, blank = True, null = True,
								verbose_name = u"Порядок сортування")

	def get_absolute_url(self):
        #parents = self._recurse_for_parents(self)
        #slug_list = [cat.slug for cat in parents]
        #if slug_list:
        #    slug_list = "/".join(slug_list) + "/"
        #else:
        #    slug_list = ""
        #return urlresolvers.reverse('satchmo_category',
        #    kwargs={'parent_slugs' : slug_list, 'slug' : self.slug})
		return '/category/'

	def __unicode__(self):
		return self.name

	def pic(self):
		if self.photo:
			return u'<img src="%s" width="70"/>' % self.photo.url
		else:
			return '(none)'

	pic.short_description = u'Зображення'
	pic.allow_tags = True

	class Meta:
		verbose_name_plural = 'Категорії'
		verbose_name = 'Категорія'

class Product(models.Model):
	name = models.CharField(max_length = 150, blank = True, verbose_name = "Назва")
	category = models.ForeignKey('Category',
								related_name = 'product')
	title = models.CharField(max_length = 200, default = "", blank = True,
								verbose_name = "Заголовок")
	meta_desc = models.CharField(max_length = 200, default = "", blank = True,
								verbose_name = "Мета опис")
	meta_key = models.CharField(max_length = 200, default = "", blank = True,
								verbose_name = "Ключові слова")
	short_description = tinymce_model.HTMLField(blank = True, verbose_name = "Короткий опис товару")
	description = tinymce_model.HTMLField(blank = True, verbose_name = "Повний опис товару")
	slug = models.CharField(max_length = 250, default = "", blank = True,
								verbose_name = "Урл")
	photo = models.ImageField(upload_to = make_upload_path, default = "", blank = True,
							verbose_name = "Зображення")
	published = models.BooleanField(verbose_name = u"Опубліковано") 
	orderin = models.IntegerField(default = 0, blank = True, null = True,
								verbose_name = u"Порядок сортування")
	date_add = models.DateTimeField(default = datetime.datetime.now(), auto_now_add = True,
									verbose_name = "Дата створення")
	manufacturer = models.CharField(max_length = 300,
									blank = True)
	price_in_ua = models.DecimalField(max_digits = 6,
									decimal_places = 2)

	#photo = models.ImageField(upload_to = 'images/%Y/%m/%d',
	#

	def __unicode__(self):
		return self.name

	def pic(self):
		if self.photo:
			return u'<img src="%s" width="70"/>' % self.photo.url
		else:
			return '(none)'

	pic.short_description = u'Зображення'
	pic.allow_tags = True

	@models.permalink
	def get_absolute_url(self):
		return ('product_detail', [str(self.id)])

	def get_category(self):
		return Category.objects.get(id = self.category)

	def get_category_name(self):
		return self.category.name

	class Meta:
		verbose_name_plural = 'Товари'
		verbose_name = 'Товар'

class ProductImages(models.Model):
	product = models.ForeignKey('Product', null = True, blank = True)
	image = models.ImageField(upload_to = make_upload_path, default = "",
							blank = True, verbose_name = "Зображення")

	def __unicode__(self):
		return self.image

	def pic(self):
		if self.image:
			return u'<img src="%s" width="70"/>' % self.image.url
		else:
			return '(none)'
	pic.short_description = u'Зображення'
	pic.allow_tags = True

	class Meta:
		verbose_name_plural = "Зображення"
		verbose_name = "Зображення"

class Customer(models.Model):
	name = models.CharField(max_length = 150, blank = True, verbose_name = "Користувач")
	#user = models.ForeignKey(User)
	email = models.EmailField(max_length = 254, blank = True, verbose_name = "Email")
	password = models.CharField(max_length = 250, blank = True, verbose_name = "Пароль")
	discaunt = models.DecimalField(max_digits = 4, default = 0, decimal_places = 2)
	date_created = models.DateTimeField(default = datetime.datetime.now(), auto_now_add = True,
										verbose_name = "Дата регістрації")
	date_visited = models.DateTimeField()
