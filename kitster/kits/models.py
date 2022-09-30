from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=200)
	social_link = models.CharField(max_length=200)
	avatar = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Kit(models.Model):
	pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	cover = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Product(models.Model):
	kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	img_url = models.CharField(max_length=200)
	yandex_market_link = models.CharField(max_length=200)
	yandex_market_link = models.CharField(max_length=200)

	def __str__(self):
		return self.name

