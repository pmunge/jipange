from django.contrib import admin

# Register your models here.

from . models import Member,Event,Contribution

admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Contribution)