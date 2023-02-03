from django import forms
from generator.models import Passwords


class AddSavePassword(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['service', 'password_for_the_service', 'user']
        widgets = {'user': forms.HiddenInput()}




