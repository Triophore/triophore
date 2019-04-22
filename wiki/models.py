from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.

class WikiCategory(models.Model):
    category = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.category
class WikiSubCategory(models.Model):
    sub_category = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.sub_category

class Wiki(models.Model):
    title = models.CharField(max_length = 100,unique=True)
    category = models.ForeignKey(WikiCategory,on_delete = models.CASCADE)
    sub_category = models.ForeignKey(WikiSubCategory,on_delete = models.CASCADE)
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    url = models.CharField(max_length = 100,unique=True)
    content = RichTextUploadingField('default')

    def __str__(self):
        return self.title