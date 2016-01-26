from django.contrib import admin
from .models import SuperHero, Wife, Address


# Register your models here.
class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ("name", 'added_on')
    search_fields = ("name",)
    ordering = ("name",)
    list_filter = ("name", "added_on")

admin.site.register(SuperHero, SuperHeroAdmin)

# Register your models here.


class WifeAdmin(admin.ModelAdmin):
    list_display = ("name", 'added_on')
    search_fields = ("name",)
    ordering = ["name"]
    list_filter = ("name", "added_on")
    raw_id_fields = ("superhero", )

admin.site.register(Wife, WifeAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", 'added_on')
    search_fields = ("city",)
    ordering = ("city",)
    list_filter = ("city", "added_on")


admin.site.register(Address, AddressAdmin)
