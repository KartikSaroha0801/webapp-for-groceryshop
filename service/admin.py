from django.contrib import admin
from .models import *
from service.models import UpdateStock

class serviceAdmin(admin.ModelAdmin):
    list_display=('Item','NumberOfItemAvailable')

admin.site.register(UpdateStock,serviceAdmin)

admin.site.register(Client)

