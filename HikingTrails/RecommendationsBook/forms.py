from django import forms
from .models import BookRecommendation

class BookRecommendationForm(forms.ModelForm):
    class Meta:
        model = BookRecommendation
        fields = ['hiker', 'title_message', 'message']
        widgets = {
            'hiker': forms.Select(),
            'title_message': forms.TextInput(attrs={'placeholder': 'Enter the title for message'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }