from .models import StudentModel
from django import forms
from django.core import validators

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=['name','email','password']
        labels={'name':'Name','email':'Email Address','password':'Password'}
        error_messages={'name':{'required':'Name is required'},'email':{'required':'Email is required'},
                        'password':{'required':'Password is required'}}
        widgets={'name':forms.TextInput(attrs={'placeholder':'enter your name'}),
                 'email':forms.EmailInput(attrs={'placeholder':'enter email'}),
                 'password':forms.PasswordInput(attrs={'placeholder':'enter password'})
                 }    
    
