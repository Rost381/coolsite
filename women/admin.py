from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'get_photo', 'is_published')
    readonly_fields = ('get_photo',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self,obj):
        '''
        :param obj:
        :return: как строку, а не как Тэг
        '''
        return  mark_safe(f'<img src={obj.photo.url} width="50", height="auto"')
    get_photo.short_description = "Фото"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
