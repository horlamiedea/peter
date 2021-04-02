from django.db import models
from django.conf import settings
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.TextField()
    def __str__(self):
        
        return self.name
     
     
class New(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    news = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    
    
class Sermon(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date = models.DateField()
    sermon = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class FirstTimer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()
    city = models.TextField()
    # state = models.TextChoices()
    about_you = models.TextField()
    
    