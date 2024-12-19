from django.urls import path

from HikingTrails.Trails.views import TrailsListView, TrailsDetailView, TrailsCreateView, TrailDeleteView, \
    CommentCreateView, TrailEditView, delete_photo

urlpatterns = [

    path('', TrailsListView.as_view(), name='trail_list'),

    path('<int:pk>/', TrailsDetailView.as_view(), name='trail_details'),

    path('photo/delete/<int:photo_id>/', delete_photo, name='delete_photo'),

    path('create/', TrailsCreateView.as_view(), name='trail_create'),

    path('<int:pk>/delete/', TrailDeleteView.as_view(), name='trail_delete'),

    # path('<int:pk>/trails_confirm_delete/', TrailEditView.as_view(), name='trails_confirm_delete'),

    path('<int:pk>/edit/', TrailEditView.as_view(), name='trail_edit'),

    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_trail'),

]
