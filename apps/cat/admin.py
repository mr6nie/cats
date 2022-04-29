import django
from django.contrib import admin

from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ["id", "uuid", "title", "location", "price"]
    list_display_links = ["id", "uuid", "title"]

admin.site.register(Cat, CatAdmin)