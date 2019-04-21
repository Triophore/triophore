from django.contrib import admin

# Register your models here.
from .models import Wiki,WikiCategory

class WikiAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at','url','is_active')

class WikiCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Wiki,WikiAdmin)
admin.site.register(WikiCategory,WikiCategoryAdmin)