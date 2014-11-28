from webshop.models import Category
from myShop import settings

def webshop(request):
	username = request.session.get('username', None)

	return {
			'shop_name': settings.WEB_SITE_NAME,
			'username' : username,
			'categorylist': Category.objects.all(),
			'request': request
	}
