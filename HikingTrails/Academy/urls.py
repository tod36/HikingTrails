from django.urls import path
from .views import MeetingCreateView, MeetingListView, MeetingPhotos, MeetingPhotosView

urlpatterns = [
    path('create/', MeetingCreateView.as_view(), name='meeting_form'),

    path('upload/', MeetingPhotosView.as_view(), name='upload_photo'),
    path('', MeetingListView.as_view(), name='photo_list'),
]