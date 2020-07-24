from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_website']
    filter_horizontal = ['machine', 'application']

    # We don't display all the company_website
    def from_url_shortcut(self, obj):
        if len(obj.company_website) > 64:
            return f'{obj.company_website[:64]} ...'
        else:
            return obj.company_website


admin.site.register(Company, CompanyAdmin)