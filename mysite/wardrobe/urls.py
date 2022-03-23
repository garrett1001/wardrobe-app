from django.urls import path
from . import views

app_name = 'wardrobe'

urlpatterns = [
    path('', views.wardrobe, name='wardrobe'),
    path('garment/upload/', views.garment_upload, name='garment_upload'),
    path('garment/<int:garment_id>/', views.garment_detail, name='garment_detail'),
    path('garment/<int:garment_id>/edit/', views.garment_edit, name='garment_edit'),
    path('garment/<int:garment_id>/delete/', views.garment_delete, name='garment_delete'),
    path('outfit/create/', views.outfit_create, name='outfit_create'),
    path('outfit/<int:outfit_id>/', views.outfit_detail, name='outfit_detail'),
    path('outfit/<int:outfit_id>/edit/', views.outfit_edit, name='outfit_edit'),
    path('outfit/<int:outfit_id>/delete/', views.outfit_delete, name='outfit_delete'),
]