from django.db import models

class AnalysisModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Otomatik oluşturulma zamanı
    updated_at = models.DateTimeField(auto_now=True)      # Otomatik güncellenme zamanı
    is_active = models.BooleanField(default=True)         # Aktiflik durumu

    def __str__(self):
        return self.name
