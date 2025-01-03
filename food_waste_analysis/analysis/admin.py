from django.contrib import admin
from .models import AnalysisModel

@admin.register(AnalysisModel)
class AnalysisModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'is_active']  # Modeldeki alanlara referans
    list_filter = ['is_active', 'created_at']  # Sadece model alanlarına referans
