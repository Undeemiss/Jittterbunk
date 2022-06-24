from django.urls import path

from . import views

app_name = 'bunk'
urlpatterns = [
    path('', views.redirect_global_feed),
    path('feed', views.GlobalFeed.as_view(), name='global_feed'),
]