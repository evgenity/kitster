from django.contrib import admin

# Register your models here.
from .models import Author, Kit, Product

admin.site.register(Author)
admin.site.register(Kit)
admin.site.register(Product)