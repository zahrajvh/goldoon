from django import forms
from .models import processing
from django.utils.translation import gettext as _


class Processing_form(forms.ModelForm):
    photo = forms.ImageField(label=_("تصویر گل"), required=True, widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = processing
        fields = "__all__"
