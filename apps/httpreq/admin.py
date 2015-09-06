from django.contrib import admin
from .models import HttpReqStore


class AdminForm(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'atime']

admin.site.register(HttpReqStore, AdminForm)
