from django.contrib import admin

from .models import Category, Portfolio, Technology

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Technology)

