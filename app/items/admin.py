from django.contrib import admin

from .models import Item, Tag, Manufacturer
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Manufacturer)