from django.contrib import admin

# Register your models here.

from . models import Member,Event

admin.site.register(Member)
admin.site.register(Event)