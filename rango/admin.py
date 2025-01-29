from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

# customise the admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
