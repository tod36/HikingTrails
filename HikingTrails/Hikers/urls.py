from django.contrib.auth.views import LoginView
from django.urls import path

from HikingTrails.Hikers import views
from HikingTrails.Hikers.views import HikerRegView, HikerDetailView

urlpatterns = [
    path('register/', HikerRegView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('hiker/<int:pk>/', HikerDetailView.as_view(), name='hiker_details'),
    path('', views.home, name='home'),
    path('home_with_nav/', views.home_with_nav, name='home_with_nav'),
]