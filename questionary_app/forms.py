import os

from django import forms

from .models import Genre


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
