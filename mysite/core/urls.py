from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('feed/', views.feed, name='feed'),
    path('settings/', views.edit_profile, name='edit_profile'),
    path('search_results/', views.search_results, name='search_results'),
    path('top_profiles', views.top_profiles_list, name='top_profiles'),
    path('profile/<str:username>/', views.profile, name='user_profile'),
    path('profile/<str:username>/follow', views.add_follower, name='add_follower'),
    path('profile/<str:username>/unfollow', views.remove_follower, name='remove_follower'),
    path('profile/<str:username>/top/<int:top_id>/', views.profile_top_detail, name='profile_top_detail'),
    path('profile/<str:username>/bottom/<int:bottom_id>/', views.profile_bottom_detail, name='profile_bottom_detail'),
    path('profile/<str:username>/outerwear/<int:outerwear_id>/', views.profile_outerwear_detail, name='profile_outerwear_detail'),
    path('profile/<str:username>/footwear/<int:footwear_id>/', views.profile_footwear_detail, name='profile_footwear_detail'),
    path('profile/<str:username>/accessory/<int:accessory_id>/', views.profile_accessory_detail, name='profile_accessory_detail'),
    path('profile/<str:username>/outfit/<int:outfit_id>/', views.profile_outfit_detail, name='profile_outfit_detail'),
    path('inbox/', views.inbox, name='inbox'),
    path('inbox/<int:message_id>/', views.inbox_detail, name='inbox_detail'),
    path('sent/', views.sent, name='sent'),
    path('sent/<int:message_id>/', views.sent_detail, name='sent_detail'),
    path('profile/<str:username>/message/', views.send_message, name='send_message'),
    path('inbox/<str:username>/reply/', views.reply_message, name='reply_message'),
]