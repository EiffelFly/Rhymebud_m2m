from django.contrib import admin
from .models import Industry

class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    filter_horizontal = ['company', 'application', 'machine' ]

    # We don't display all the company_website
    def description_shortcut(self, obj):
        if len(obj.description) > 64:
            return f'{obj.description[:64]} ...'
        else:
            return obj.description


admin.site.register(Industry, IndustryAdmin)
