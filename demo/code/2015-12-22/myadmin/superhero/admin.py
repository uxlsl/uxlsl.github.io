from django.contrib import admin
from .models import SuperHero


# Register your models here.
class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ("name", 'added_on')
    search_fields = ["name"]
    ordering = ["name"]
    list_filter = ("name", "added_on")

admin.site.register(SuperHero, SuperHeroAdmin)
