from django.urls import path
from . import views

urlpatterns = [
    path('campaign/new/', views.campaign_form, name='campaign_form'),
    path('user/new/', views.user_form, name='user_form'),
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('users/', views.user_list, name='user_list'),
    
    # API
    path('api/campaign/', views.api_campaign, name='api_campaign'),
    path('api/user/', views.api_user, name='api_user'),
]
