import datetime

from django.contrib.auth.models import User
from django.db import models

from HikingTrails import settings
from HikingTrails.Hikers.models import Hiker
from HikingTrails.Trails.validators import validate_image


class Meeting(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return self.year


class MeetingPhotos(models.Model):
    current_year = datetime.datetime.now().year
    YEAR_CHOICES = [(r, r) for r in range(2008, current_year + 1)]

    meeting = models.PositiveIntegerField(choices=YEAR_CHOICES)
    image = models.ImageField(upload_to='meeting_photos/', validators=[validate_image])
    uploaded_by = models.ForeignKey(Hiker, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Photo from {self.meeting} by {self.uploaded_by.username}"


class CommentMeeting(models.Model):
    meeting = models.ForeignKey(to=Meeting, on_delete=models.CASCADE, related_name='meeting_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.meeting}'
