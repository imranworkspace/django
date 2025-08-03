from django import forms
from django.core import validators

class StudentForm(forms.Form):
    name=forms.CharField(label='Student Name',label_suffix=":",
                         validators=[validators.MinLengthValidator(3),
                         validators.MaxLengthValidator(10)],
                         widget=forms.TextInput(attrs={'placeholder':'Enter Name'}),
                         error_messages={'required':'Name is required'})
    email=forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'placeholder':'Enter Email Address'}),
                           error_messages={'required':'Email is required'})
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}),
                             error_messages={'required':'Password is required'},
                             validators=[validators.MinLengthValidator(8),
                             validators.MaxLengthValidator(16)])
                             
    