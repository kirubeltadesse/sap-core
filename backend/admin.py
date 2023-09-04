from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "student", "mentor", "start_date", "end_date", "status")
    list_filter = ("status", "date_posted", "start_date", "end_date")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("student", "mentor")
    date_hierarchy = "start_date"
    ordering = ("status", "start_date")


admin.site.register(models.Category)
# Register your models here.

admin.site.register(models.Mainuser)

admin.site.register(models.Student)
