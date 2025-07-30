from typing import Any
from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(label='Student Name',label_suffix=':',max_length=25,
                         widget=forms.TextInput(attrs={'placeholder':'Enter Name'}))
    email=forms.EmailField(label='Email',required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))

    # for all fields
    '''def clean(self):
        cleaned_data = super().clean()
        name=cleaned_data.get('name')
        em=cleaned_data.get('email')
        pw=cleaned_data.get('password')

        if pw and len(pw) < 8:
            self.add_error('password','password length should be more than 8 characters')
        return cleaned_data '''
    # for specific_fields
    def clean_password(self):
        pw=self.cleaned_data['password']
        if len(pw) < 8: 
            raise forms.ValidationError('password length should be more than 8 characters')
        return pw