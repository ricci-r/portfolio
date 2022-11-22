from django.contrib import admin

from .models import Category, Portfolio, Technology

# Register your models here.

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
        }

admin.site.register(Category)
admin.site.register(Technology)

