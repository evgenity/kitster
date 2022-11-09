from django.db import models
from django.urls import reverse

class Author(models.Model):
	name = models.CharField(max_length=200)
	social_link = models.CharField(max_length=200)
	avatar = models.FileField(upload_to='authors')
	hero_cover = models.FileField(upload_to='authors', default='static/1500x500.png')
	pro = models.BooleanField(default=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200)
	class_addon = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Kit(models.Model):
	pub_date = models.DateTimeField('date published')
	tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=True)
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.PROTECT)
	cover = models.FileField(upload_to='kits')
	hero_cover = models.FileField(upload_to='kits', default='static/1500x500.png')
	class_addon = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		url = reverse('kits:detail', args=[self.id] )
		return url

class Product(models.Model):
	kit = models.ForeignKey(Kit, on_delete=models.PROTECT)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	img_url = models.FileField(upload_to='products', max_length=255)
	yandex_market_link = models.CharField(max_length=200)
	other_link = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name

class KitHit(models.Model):
	pub_date = models.DateTimeField('date hit')
	kit = models.ForeignKey(Kit, on_delete=models.PROTECT)
	ip = models.CharField(max_length=15)

	@staticmethod
	def get_client_ip(request):
	    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	    if x_forwarded_for:
	        ip = x_forwarded_for.split(',')[0]
	    else:
	        ip = request.META.get('REMOTE_ADDR')
	    return ip

	def __str__(self):
		return ' '.join(map(str, [self.pub_date, self.kit, self.ip]))