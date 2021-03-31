from django.contrib import admin
from .models import Event, New, Sermon

# Register your models here.
admin.site.register(Event)
admin.site.register(Sermon)
admin.site.register(New)