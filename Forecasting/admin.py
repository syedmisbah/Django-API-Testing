from django.contrib import admin
from django import forms
from .models import BaseTable

class BaseTableAdminForm(forms.ModelForm):

    class Meta:
        model = BaseTable
        fields = '__all__'


class BaseTableAdmin(admin.ModelAdmin):
    form = BaseTableAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'CustomerID', 'Account']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'CustomerID', 'Account']

admin.site.register(BaseTable, BaseTableAdmin)


