from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('search_results/', views.search_results, name='search_results'),
    path('profile/<str:username>/', views.profile, name='user_profile'),
    path('profile/<str:username>/garment/<int:garment_id>/', views.profile_garment_detail, name='profile_garment_detail'),
    path('profile/<str:username>/outfit/<int:outfit_id>/', views.profile_outfit_detail, name='profile_outfit_detail'),
]