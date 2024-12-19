from django import forms

from .models import Meeting, MeetingPhotos, CommentMeeting


class CommentMeetingForm(forms.ModelForm):
    class Meta:
        model = CommentMeeting
        fields = '__all__'


class MeetingPhotosForm(forms.ModelForm):
    class Meta:
        model = MeetingPhotos
        fields = '__all__'


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
