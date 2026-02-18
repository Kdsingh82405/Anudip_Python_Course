from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .models import Customer

# ----------------  CUSTOMER LOGIN FORM SECTION -----------------------------------------------------------------------------------
class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete':'current-password',
            'placeholder': 'Password'
        })
    )

# ----------------  CUSTOMER RESGISRTATION FORM SECTION -----------------------------------------------------------------------------------
class CustomerRegistrationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': 'True',
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
# ----------------  PASSWORD CHANGE FORM SECTION -----------------------------------------------------------------------------------

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={
            'autofocus': 'True',
            'autocomplete': 'current-password',
            'class': 'form-control'
        })
    )

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control'
        })
    )

    new_password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control'
        })
    )

# ----------------  CHANGE PASSWORD-RESET FORM SECTION -----------------------------------------------------------------------------------

# ---------------- PASSWORD RESET FORM ----------------
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your registered email'
            }
        )
    )


# ---------------- SET NEW PASSWORD FORM ----------------
class MySetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control',
                'placeholder': 'New Password'
            }
        )
    )

    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }
        )
    )



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=['name','locality','city','mobile','state','zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }