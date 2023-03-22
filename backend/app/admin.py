from django.contrib import admin

from . models import Organization, Shop


admin.site.register(Shop)


class ShopsInline(admin.StackedInline):
    model = Shop


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ShopsInline]

