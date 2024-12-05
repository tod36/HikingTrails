from django.urls import path

from HikingTrails.Trails.views import TrailsListView, TrailsDetailView, TrailsCreateView, TrailDeleteView, \
    CommentCreateView, TrailEditView

urlpatterns = [

    path('', TrailsListView.as_view(), name='trail_list'),

    path('<int:pk>/', TrailsDetailView.as_view(), name='trail_details'),

    path('create/', TrailsCreateView.as_view(), name='trail_create'),

    path('<int:pk>/delete/', TrailDeleteView.as_view(), name='trail_delete'),

    path('<int:pk>/edit/', TrailEditView.as_view(), name='trail_edit'),

    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_trail'),

]
