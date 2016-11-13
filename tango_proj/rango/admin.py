from django.contrib import admin
from tango_proj.rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'view', 'likes')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CatAdmin)
admin.site.register(Page, PageAdmin)

