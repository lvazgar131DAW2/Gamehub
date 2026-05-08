from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'image', 'category', 'release_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del juego'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del juego',
                'rows': 5
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'release_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['description'].label = 'Descripción'
        self.fields['image'].label = 'Imagen'
        self.fields['category'].label = 'Categoría'
        self.fields['release_date'].label = 'Fecha de lanzamiento'
