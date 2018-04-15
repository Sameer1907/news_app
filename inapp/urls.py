from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.latest_news, name = 'latest_news'),
    url('sports/', views.sports_news, name = 'sports_news'),
    url('business/', views.business_news, name = 'business_news'),
    url('entertainment/', views.entertainment_news, name = 'entertainment_news'),
    url('health/', views.health_news, name = 'health_news'),
    url('technology/', views.technology_news, name = 'technology_news'),
    url('general/', views.general_news, name = 'general_news'),
    url('science/', views.science_news, name = 'science_news'),
    url('search/', views.search_news, name = 'search_news'),
]
