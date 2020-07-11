from django.contrib import admin
from .models import Empresa, Sector
# Register your models here.

class SectorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'ticker')

admin.site.register(Empresa)
admin.site.register(Sector,SectorAdmin)