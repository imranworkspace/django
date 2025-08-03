from django import forms
from .models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=['name','email','password']
        labels={'name':'Student Name','email':'Email Address','password':'Password'}
        widgets={'name':forms.TextInput(attrs={'placeholder':'enter your name','class': 'form-control'}),
                'email':forms.EmailInput(attrs={'placeholder':'enter your email','class': 'form-control'}),
                'password':forms.PasswordInput(attrs={'placeholder':'enter your password','class': 'form-control'}),
                'created_at':forms.DateTimeInput(),'updated_at':forms.DateTimeInput()}
        error_message={'name':'Enter Name','email':'Enter email','password':'Enter password'}

