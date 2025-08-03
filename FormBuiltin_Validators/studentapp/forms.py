from typing import Any
from django import forms
# builtin validators
from django.core import validators

#custom validator
def stars_with_i(value):
    raise forms.ValidationError('email should be starts with "i"')

class StudentForm(forms.Form):
    name=forms.CharField(label='Student Name',
                         validators=[validators.MinLengthValidator(3),validators.MaxLengthValidator(10)],
                         widget=forms.TextInput(attrs={'placeholder':'your name'})) # builtin validators
    
    email=forms.EmailField(label='Email',validators=[stars_with_i],
                           widget=forms.EmailInput(attrs={'placeholder':'your email'})) #custom validator

    