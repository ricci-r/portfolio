from django.contrib import admin

from .models import Category, Portfolio

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Category)

