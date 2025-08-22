from django import forms


# for specific_fields
def start_with_i(value):
    raise forms.ValidationError('name should be starts with i')


class StudentForm(forms.Form):
    # name=forms.CharField(max_length=25,validators=[start_with_i],widget=forms.TextInput(attrs={'placeholder':'enter student name'}),
    name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'placeholder':'enter student name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'enter email'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))

     # for specific_fields
    '''def clean_name(self):
        nm=self.cleaned_data['name']
        if nm[0]!='i': 
            raise forms.ValidationError('name should be starts with i')
        return nm
    
    def clean_password(self):
        pw=self.cleaned_data['password']
        if len(pw)<8:
            raise forms.ValidationError('password length should be minimum 8 characters')
        return pw'''
    
    # for all fields 
    '''def clean(self):
        cleaned_data=super().clean()
        nm=cleaned_data.get('name')
        pw=cleaned_data.get('password')
        if nm and nm[0]!='i': 
            self.add_error('name','name should be starts with i')
        
        if pw and len(pw)<8:
            self.add_error('password','password length should be minimum 8 characters')

        return cleaned_data  
'''

class LoginForm(forms.Form):
    name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'placeholder':'enter student name'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))
