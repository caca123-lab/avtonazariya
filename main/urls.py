from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),

    # WebApp yo'nalishlari
    path('webapp/', views.webapp_home, name='webapp_home'),
    path('webapp/dashboard/', views.webapp_dashboard, name='webapp_dashboard'),
    path('webapp/test/', views.webapp_test, name='webapp_test'),
    path('webapp/practice/', views.webapp_practice, name='webapp_practice'),
    path('webapp/topics/', views.webapp_topics, name='webapp_topics'),
    path('webapp/results/', views.webapp_results, name='webapp_results'),
    path('webapp/statistics/', views.webapp_statistics, name='webapp_statistics'),
    path('webapp/profile/', views.webapp_profile, name='webapp_profile'),
    path('webapp/loading/', views.webapp_loading, name='webapp_loading'),
]
