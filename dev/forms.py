from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django import forms

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # Add phone number field with validator
    phone_number_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
    )
    
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        validators=[phone_number_validator],
        required=True,
        help_text="e.g., +2348012345678"
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number',)