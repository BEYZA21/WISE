from django.contrib import admin
from django.urls import path, include  # include fonksiyonu eklendi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # users uygulamasındaki urls.py dosyasını dahil et
]
