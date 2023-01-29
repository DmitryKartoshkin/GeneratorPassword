from django import forms
from generator.models import Password


class AddSavePassword(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['service', 'password_for_the_service']




