from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import CsvModel

@admin.register(CsvModel)
class PersonAdmin(ImportExportModelAdmin):
    pass