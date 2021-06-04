from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Registration, Contact, Newsletter)
class ViewAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
