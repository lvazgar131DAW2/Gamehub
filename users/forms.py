from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

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
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

        self.fields['username'].help_text = (
            'Requerido. 150 caracteres o menos. '
            'Solo letras, números y @/./+/-/_'
        )

        self.fields['password1'].help_text = '''
        <ul style="margin-bottom: 0;">
            <li>Tu contraseña no puede ser muy parecida a tu información personal.</li>
            <li>Tu contraseña debe contener al menos 8 caracteres.</li>
            <li>Tu contraseña no puede ser completamente numérica.</li>
            <li>Las contraseñas comunes no están permitidas.</li>
        </ul>
        '''

        self.fields['password2'].help_text = (
            'Introduce la misma contraseña nuevamente para verificación.'
        )

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Este nombre de usuario ya está registrado.'
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este correo electrónico ya está registrado.'
            )

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Las contraseñas no coinciden.'
            )

        return password2


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        label='Recordarme',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })