from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    filter_horizontal = ['machine']

     # We don't display all the application description
    def description_shortcut(self, obj):
        if len(obj.description) > 32:
            return f'{obj.description[:32]} ...'
        else:
            return obj.description

admin.site.register(Application, ApplicationAdmin)