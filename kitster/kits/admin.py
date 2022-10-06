from django.contrib import admin

# Register your models here.
from .models import Author, Kit, Product, Tag, KitHit

admin.site.register(Author)
admin.site.register(Kit)
admin.site.register(Product)
admin.site.register(Tag)

class KitHitAdmin(admin.ModelAdmin):
    list_display= ('pub_date', 'kit', 'ip')

admin.site.register(KitHit, KitHitAdmin)