from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length = 20,blank=True)
    phone = models.CharField(max_length = 20,blank=True)
    email = models.EmailField(max_length = 20,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
