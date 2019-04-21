from django.contrib import admin

# Register your models here.
from . import models

class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'message')
    list_filter = (
        'email',
        'full_name',
    )
    search_fields = (
        'email',
        'full_name',
    )

admin.site.register(models.Message,MessageAdmin)