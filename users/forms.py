from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre (opcional)'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido (opcional)'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Nombre de usuario'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

        self.fields['username'].help_text = 'Requerido. 150 caracteres o menos. Solo letras, números y @/./+/-/_'
        self.fields['password1'].help_text = '''<ul style="margin-bottom: 0;">
            <li>Tu contraseña no puede ser muy parecida a tu nombre de usuario.</li>
            <li>Tu contraseña debe contener al menos 8 caracteres.</li>
            <li>Tu contraseña no puede ser un número completamente.</li>
            <li>Las contraseñas comunes no se permiten.</li>
        </ul>'''
        self.fields['password2'].help_text = 'Por favor escribe la misma contraseña nuevamente.'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        return email


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })

