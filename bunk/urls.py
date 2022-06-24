from django.urls import path

from . import views

app_name = 'bunk'
urlpatterns = [
    path('', views.redirect_global_feed),
    path('feed', views.GlobalFeed.as_view(), name='global_feed'),
    path('<int:user_id>/feed/', views.user_feed, name='user_feed'),
    path('<int:to_user_id>/bunk/', views.bunk_submit, name='bunk_submit'),
]