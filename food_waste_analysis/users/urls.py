from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa
    path('register/', views.register, name='register'),  # Kayıt ol
    path('login/', views.login, name='login'),  # Giriş
    path('logout/', views.logout, name='logout'),  # Çıkış
    path('panel/', views.panel, name='panel'),
    path("view_results/", views.view_results, name="view_results"),  # URL tanımı
    path("view_graphs/", views.view_graphs, name="view_graphs"),
    path("upload_images/", views.upload_images, name="upload_images"),
     path("genarate_report/", views.genarate_report, name="genarate_report")
]

