from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.

MENU_DIRECTION = (
    ('Left','Left'),
    ('Right','Right')
)

class Details(models.Model):
    author = models.CharField(max_length = 100,null = True, blank = True)
    description = models.TextField(max_length = 1000,null = True, blank = True)
    keywords = models.TextField(max_length = 1000,null = True, blank = True)
    def __str__(self):
        return self.author

class MainMenu(models.Model):
    title = models.CharField(max_length = 25,unique=True)
    url = models.CharField(max_length = 100,blank = True)
    direction = models.CharField(max_length = 10,choices = MENU_DIRECTION,default = 'Left')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    class Meta(object):
        ordering = ['order']
    def __str__(self):
        return self.title

class SubMenuCategory(models.Model):
    name = models.CharField(max_length = 25,unique=True)
    order = models.IntegerField(default=0)
    class Meta(object):
        ordering = ['order']
    def __str__(self):
        return self.name

class SubMenu(models.Model):
    title = models.CharField(max_length = 25)
    parent = models.ForeignKey(MainMenu,on_delete = models.CASCADE)
    category = models.ForeignKey(SubMenuCategory,on_delete = models.CASCADE)
    url = models.CharField(max_length = 100,blank = True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    class Meta(object):
        ordering = ['order']
    def __str__(self):
        return self.title


class MenuItemCategory(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    order = models.PositiveIntegerField(_('order'), default=0, blank=False, null=False)
    url = models.CharField(max_length = 30,null = True)
    class Meta(object):
        ordering = ('order',)
        verbose_name = _('menu item category')
        verbose_name_plural = _('menu item categories')

    def __str__(self):
        return self.title


class MenuItem(MPTTModel):
    name = models.CharField(_('name'), max_length=50, unique=True)
    parent = TreeForeignKey('self', verbose_name=_('parent menu item'), null=True, blank=True, related_name='children', db_index=True,on_delete=models.PROTECT)
    order = models.PositiveIntegerField(_('order'), default=0, blank=False, null=False)
    category = models.ForeignKey(MenuItemCategory, verbose_name=_('category'),on_delete=models.PROTECT)
    url = models.CharField(max_length = 30, null = True)
    class Meta(object):
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')
        ordering = ('order',)

    class MPTTMeta:
        order_insertion_by = ('name',)

    def __str__(self):
        return self.name
