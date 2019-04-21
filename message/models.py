from django.db import models

# Create your models here.

class Message(models.Model):
    email = models.EmailField(max_length = 200)
    full_name = models.CharField(max_length = 100)
    message = models.TextField(max_length= 500,null = True)

    def __str__(self):
        return self.email
    