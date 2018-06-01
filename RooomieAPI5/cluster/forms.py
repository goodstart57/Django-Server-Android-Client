from django import forms
from .models import MemInfo


class MemInfoForm(forms.ModelForm):
    class Meta:
        model = MemInfo
        fields = ['STUD_ID', 'ID', 'PWD', 'NAME', 'GENDER', 'PHONE', 'EMAIL', 'MAJOR']
