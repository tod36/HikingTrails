from django.db import models
from HikingTrails.Hikers.models import Hiker

class BookRecommendation(models.Model):
    hiker = models.ForeignKey(Hiker, on_delete=models.CASCADE)
    title_message = models.CharField(max_length=200)
    message = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title_message
