from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(label='Student Name',label_suffix=':',max_length=25,
                         widget=forms.TextInput(attrs={'placeholder':'Enter Name'}))
    email=forms.EmailField(label='Email',required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))