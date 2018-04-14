from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.latest_news, name = 'latest_news'),
    path('sports/', views.sports_news, name = 'sports_news'),
    path('business/', views.business_news, name = 'business_news'),
    path('entertainment/', views.entertainment_news, name = 'entertainment_news'),
    path('health/', views.health_news, name = 'health_news'),
    path('technology/', views.technology_news, name = 'technology_news'),
    path('general/', views.general_news, name = 'general_news'),
    path('science/', views.science_news, name = 'science_news'),
    path('search/', views.search_news, name = 'search_news'),
=======
    url('post_list', views.post_list, name='post_list'),
    url('', views.latest_news, name = 'latest-news')
>>>>>>> 4d957bbabed388f0bdd4e3b1d6493fc75d02687e
]
