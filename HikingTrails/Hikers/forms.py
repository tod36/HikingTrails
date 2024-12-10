from django import forms
from django.contrib.auth.forms import UserCreationForm

from HikingTrails.Hikers.models import Hiker


# class HikerRegForm(UserCreationForm):
#     class Meta:
#         model = Hiker
#         fields = ['username', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={'placeholder': 'Enter your username or nickname'}
#             ),
#         }


class HikerRegForm(UserCreationForm):
    class Meta:
        model = Hiker
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username or nickname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
        }


from django import forms
from HikingTrails.Hikers.models import Hiker


# class HikerDetailForm(forms.ModelForm):
#     class Meta:
#         model = Hiker
#         # exclude = ['username', 'email']
#         fields = ['first_name', 'last_name', 'age', 'phone', 'address', 'hiker_image']
#         widgets = {
#             # 'username': forms.TextInput(attrs={'placeholder': 'You cannot change your username', 'disabled': True}),
#             'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
#             # 'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'disabled': True}),
#             'age': forms.NumberInput(attrs={'placeholder': 'Enter your age'}),
#             'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
#             'address': forms.Textarea(attrs={'placeholder': 'Enter your address'}),
#             'hiker_image': forms.FileInput(),
#         }


class HikerDetailForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ['first_name', 'last_name', 'email', 'age', 'phone', 'address', 'hiker_image']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter your age'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter your address'}),
            'hiker_image': forms.FileInput(),
        }
