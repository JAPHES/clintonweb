from django.urls import path
from . import views

# the project urls

urlpatterns = [
    path('health/', views.health),
    path('', views.home, name='home'),                  # Home Page
    path('projects/', views.projects, name='projects'), # Projects Page
    path('contact/', views.contact, name='contact'),    # Contact Me Page
    path('download-cv/', views.download_cv, name='download_cv'),
]
