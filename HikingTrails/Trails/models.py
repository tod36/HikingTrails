from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from HikingTrails.Hikers.models import Hiker
from HikingTrails.Trails.validators import validate_image


class Trails(models.Model):
    class Difficulty(models.TextChoices):
        EASY = 'Easy', 'Easy'
        INTERMEDIATE = 'Intermediate', 'Intermediate'
        UPHILL = 'Uphill', 'Uphill'

    name = models.CharField(max_length=100)
    length = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True, blank=True, validators=[validate_image])
    difficulty = models.TextField(
        choices=Difficulty.choices,
        default=Difficulty.EASY,
    )
    description = models.TextField(help_text='Enter a description of the trail')
    elevation_gain = models.FloatField(null=True, blank=True)
    hiker = models.ForeignKey(Hiker, on_delete=models.CASCADE, related_name='trails')
    created_at = models.DateTimeField(auto_now_add=True)

    # Add other fields as necessary

    def __str__(self):
        return self.name


class Comment(models.Model):
    trail = models.ForeignKey(to=Trails, on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(Hiker, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # hiker_id = models.ForeignKey(to=Hiker, on_delete=CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.trail}'
