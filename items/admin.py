from django.contrib import admin

from items.models import Category, Comment, Item

# Register your models here.
admin.site.register([Item, Category, Comment])