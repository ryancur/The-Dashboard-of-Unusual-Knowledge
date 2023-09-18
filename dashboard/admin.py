from django.contrib import admin
from dashboard.models import Analysis


# Register your models here.
@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "picture", "description")
