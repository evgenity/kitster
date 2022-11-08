from django.contrib import admin

# Register your models here.
from .models import Author, Kit, Product, Tag, KitHit

admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Tag)

class ProductInline(admin.TabularInline):
    model = Product

class KitAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]

admin.site.register(Kit, KitAdmin)


class KitHitAdmin(admin.ModelAdmin):
    list_display= ('pub_date', 'kit', 'ip')

admin.site.register(KitHit, KitHitAdmin)