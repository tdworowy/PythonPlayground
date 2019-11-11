
from django import forms

from dlinks.models import SkypeData


class SkypeDataForm(forms.ModelForm):
    class Meta:
        model = SkypeData
        #fields = ('login', 'password', 'chatName')
        fields = ('chatName',)