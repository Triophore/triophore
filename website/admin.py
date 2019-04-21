from django.contrib import admin
#from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register your models here.
from .models import MenuItemCategory, MenuItem,MainMenu,SubMenu,SubMenuCategory,Details
from mptt.admin import MPTTModelAdmin 
from django.utils.translation import ugettext_lazy as _
from adminsortable2.admin import SortableAdminMixin

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'keywords')

class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'direction','order','is_active')
    #ordering = ['order']

class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url','parent' ,'category','order','is_active')
    #ordering = ['order']

class SubMenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','order')

class MenuItemAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

'''
class MenuItemCategoryMenuItemsInline(SortableInlineAdminMixin, admin.StackedInline):
    model = MenuItem
    extra = 1
    show_change_link = True


class MenuItemCategoryMenuItemsInline2(SortableInlineAdminMixin, admin.TabularInline):
    model = MenuItem
    extra = 1
    show_change_link = True


class MenuItemCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (MenuItemCategoryMenuItemsInline,MenuItemCategoryMenuItemsInline2)
'''

#admin.site.register(MenuItem, MenuItemAdmin)
#admin.site.register(MenuItemCategory, MenuItemCategoryAdmin)

admin.site.register(Details,DetailsAdmin)
admin.site.register(MainMenu,MainMenuAdmin)
admin.site.register(SubMenu,SubMenuAdmin)
admin.site.register(SubMenuCategory,SubMenuCategoryAdmin)
