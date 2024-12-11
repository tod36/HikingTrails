from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from HikingTrails.Hikers import views
from HikingTrails.Hikers.views import HikerRegView, HikerDetailView
from HikingTrails.Hikers.views import approved_hikers, HikerUpdateView, HikerDeleteView

urlpatterns = [
    path('register/', HikerRegView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path('approved_users/', approved_hikers, name='approved_hikers'),

    path('hiker/<int:pk>/', HikerDetailView.as_view(), name='hiker_details'),

    path('hiker_update/<int:pk>/', HikerUpdateView.as_view(), name='hiker_update'),

    path('hiker/<int:pk>/delete/', HikerDeleteView.as_view(), name='hiker_delete'),
    path('', views.home, name='home'),
    path('home_with_nav/', views.home_with_nav, name='home_with_nav'),
]
