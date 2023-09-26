from django.contrib import admin

from .models import Category

from .models import Book

# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Categoryadmin)

class Bookadmin(admin.ModelAdmin):
    list_display = ['name','slug','rating','author','price','stock','available','created','updated']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Book,Bookadmin)