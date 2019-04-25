from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.models import Group
from import_export.admin import ImportExportMixin
import csv

from .models import Todo


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class TodoAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("title", "description", "created_at", "modified_at", "status")
    list_filter = ("title", "description", "created_at", "modified_at", "status")

    add_fieldsets = ()
    search_fields = ("title", "description", "created_at", "modified_at", "status")
    ordering = ()
    filter_horizontal = ()

    actions = ["export_as_csv"]


admin.site.register(Todo, TodoAdmin)
admin.site.unregister(Group)
