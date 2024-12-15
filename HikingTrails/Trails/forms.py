# forms.py
from django import forms

from .models import Comment, TrailPhotos, Trails


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class TrailPhotosForm(forms.ModelForm):
    class Meta:
        model = TrailPhotos
        fields = ['image', 'description']


class TrailForm(forms.ModelForm):
    class Meta:
        model = Trails
        exclude = ['hiker']
