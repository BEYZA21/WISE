from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Kullanıcı modelini admin paneline kaydet
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Görüntülenecek sütunlar
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # Filtreleme seçenekleri
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Arama yapılabilir alanlar
    ordering = ('username',)  # Sıralama

# Kullanıcı modelini özelleştir ve kaydet
admin.site.unregister(User)  # Varsayılan User modelini kaldır
admin.site.register(User, CustomUserAdmin)  # Özelleştirilmiş User modelini ekle
