from django import forms
from reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text'] # Поля, которые заполнит юзер