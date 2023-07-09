from django import forms
from CRUDOperation.models import locationModel
from CRUDOperation.models import dcompanyModel

class locforms(forms.ModelForm):
    class Meta:
        model=locationModel
        fields="__all__"

class comforms(forms.ModelForm):
    class Meta:
        model=dcompanyModel
        fields="__all__"