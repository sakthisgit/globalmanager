from django.contrib import admin

from .models import GmData, GmValue

# Register your models here.

admin.site.register(GmData)
admin.site.register(GmValue)

