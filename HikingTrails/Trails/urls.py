from django.urls import path

from HikingTrails.Trails.views import TrailsListView, TrailsDetailView, TrailsCreateView, CommentCreateView, \
    TrailDeleteView

urlpatterns = [
    path('', TrailsListView.as_view(), name='trail_list'),
    path('<int:pk>/', TrailsDetailView.as_view(), name='trails_detail'),
    path('create/', TrailsCreateView.as_view(), name='trails_create'),

    path('<int:pk>/delete/', TrailDeleteView.as_view(), name='trail_delete'),

    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_trail'),
]
