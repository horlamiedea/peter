from django.db import models
from django.conf import settings
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    def __str__(self):
        
        return self.name
     
     
class New(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    news = models.TextField(blank=True, null=True)
    
    
class Sermon(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date = models.DateField()
    sermon = models.TextField(blank=True, null=True)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()
    