from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=Review.RATING_CHOICES, attrs={
                'class': 'form-check-input rating-input'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu reseña...',
                'rows': 5
            }),
        }

