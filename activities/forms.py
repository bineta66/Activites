from django import forms
from .models import Journal, Categorie
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['titre', 'contenu', 'categorie', 'capture', 'statut']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'capture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }







class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Nom d'utilisateur"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'description', 'couleur']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'couleur': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        }




class InscriptionForm(forms.ModelForm):

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        }),
        help_text=''
    )

    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        }),
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom d'utilisateur"
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }

        labels = {
            'username': "Nom d'utilisateur",
            'email': 'Adresse email',
        }

        help_texts = {
            'username': '',
            'email': '',
        }

