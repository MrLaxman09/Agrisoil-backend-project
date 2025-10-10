from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = [
            'user_first_name',
            'user_last_name',
            'user_phone_no',
            'user_email',
            'user_password',
            'user_confirm_password',
            'user_Aadhar',
            'user_location'
        ]
        widgets = {
            'user_password': forms.PasswordInput(),
            'user_confirm_password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("user_password")
        confirm_password = cleaned_data.get("user_confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
