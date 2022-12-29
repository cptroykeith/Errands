from django import forms
from .models import errands


class errandsForm(forms.ModelForm):

    class Meta:
        model = errands

        fields = ['title', 'description', 'is_completed']
         