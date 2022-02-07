from django import forms
from .models import Hadir
# DataFlair


class HadirCreate(forms.ModelForm):
    class Meta:
        model = Hadir
        fields = ('nip', 'nama')
