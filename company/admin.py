from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_website']
    filter_horizontal = ['machine', 'application']

    # We don't display all the company_website
    def from_url_shortcut(self, obj):
        if len(obj.from_url) > 64:
            return f'{obj.from_url[:64]} ...'
        else:
            return obj.from_url


admin.site.register(Company, CompanyAdmin)