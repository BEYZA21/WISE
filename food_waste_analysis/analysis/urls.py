from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # User authentication routes
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Analysis routes
    path('upload-image/', views.upload_image, name='upload_image'),
    path('view-graphs/', views.view_graphs, name='view_graphs'),
    path('view-results/', views.view_results, name='view_results'),
    path('generate-reports/', views.generate_reports, name='generate_reports'),

    # Admin panel route
    path('admin/', admin.site.urls),
]
