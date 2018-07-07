from django.contrib import admin
from .models import Form
# Register your models here.


class FormAdmin(admin.ModelAdmin):
    list_display = ('date', 'name')


admin.site.register(Form)
