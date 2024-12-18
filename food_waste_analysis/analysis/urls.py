from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa
    path('upload/', views.upload, name='upload'),  # Resim yükleme
    path('graphs/', views.graphs, name='graphs'),  # Grafikler
    path('results/', views.results, name='results'),  # Sonuçlar
    path('report/', views.report, name='report'),  # Rapor oluşturma
]
