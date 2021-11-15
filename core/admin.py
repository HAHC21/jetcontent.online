from django.contrib import admin

from core.models import *


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefix')


admin.site.register(Site, SiteAdmin)
