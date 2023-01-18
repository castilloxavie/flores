from django import forms
from .models import Rosa

#formulario dinamico
class RosaForm(forms.ModelForm):
    class Meta:
        model = Rosa
        fields = '__all__'