from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'url', 'parent', 'order']
    list_filter = ['parent']

admin.site.register(MenuItem, MenuItemAdmin)

