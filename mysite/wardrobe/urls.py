from django.urls import path
from . import views

app_name = 'wardrobe'

urlpatterns = [
    path('', views.wardrobe, name='wardrobe'),
    # Garment Upload
    path('top/upload/', views.top_upload, name='top_upload'),
    path('bottom/upload/', views.bottom_upload, name='bottom_upload'),
    path('outerwear/upload/', views.outerwear_upload, name='outerwear_upload'),
    path('footwear/upload/', views.footwear_upload, name='footwear_upload'),
    path('accessory/upload/', views.accessory_upload, name='accessory_upload'),
    # Garment Detail
    path('top/<int:top_id>/', views.top_detail, name='top_detail'),
    path('bottom/<int:bottom_id>/', views.bottom_detail, name='bottom_detail'),
    path('outerwear/<int:outerwear_id>/', views.outerwear_detail, name='outerwear_detail'),
    path('footwear/<int:footwear_id>/', views.footwear_detail, name='footwear_detail'),
    path('accessory/<int:accessory_id>/', views.accessory_detail, name='accessory_detail'),
    # Garment Edit
    path('top/<int:top_id>/edit/', views.top_edit, name='top_edit'),
    path('bottom/<int:bottom_id>/edit/', views.bottom_edit, name='bottom_edit'),
    path('outerwear/<int:outerwear_id>/edit/', views.outerwear_edit, name='outerwear_edit'),
    path('footwear/<int:footwear_id>/edit/', views.footwear_edit, name='footwear_edit'),
    path('accessory/<int:accessory_id>/edit/', views.accessory_edit, name='accessory_edit'),
    # Garment Delete
    path('top/<int:top_id>/delete/', views.top_delete, name='top_delete'),
    path('bottom/<int:bottom_id>/delete/', views.bottom_delete, name='bottom_delete'),
    path('outerwear/<int:outerwear_id>/delete/', views.outerwear_delete, name='outerwear_delete'),
    path('footwear/<int:footwear_id>/delete/', views.footwear_delete, name='footwear_delete'),
    path('accessory/<int:accessory_id>/delete/', views.accessory_delete, name='accessory_delete'),
    # Outfit
    path('outfit/create/', views.outfit_create, name='outfit_create'),
    path('outfit/<int:outfit_id>/', views.outfit_detail, name='outfit_detail'),
    path('outfit/<int:outfit_id>/edit/', views.outfit_edit, name='outfit_edit'),
    path('outfit/<int:outfit_id>/delete/', views.outfit_delete, name='outfit_delete'),
]