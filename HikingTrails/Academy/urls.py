from django.urls import path

from .views import MeetingCreateView, MeetingListView, MeetingPhotosView, MeetingPhotosDeleteView

urlpatterns = [
    path('create/', MeetingCreateView.as_view(), name='meeting_form'),

    path('upload/', MeetingPhotosView.as_view(), name='upload_photo'),

    path('delete/<int:pk>/', MeetingPhotosDeleteView.as_view(), name='delete_photo'),

    path('', MeetingListView.as_view(), name='photo_list'),
]
