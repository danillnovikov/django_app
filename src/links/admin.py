from django.contrib import admin

# Register your models here.

from . import models

class LinksAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'links'
    ]

admin.site.register(models.Links, LinksAdmin)