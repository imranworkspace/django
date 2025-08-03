from django import forms
from django.core.validators import MinLengthValidator

class StudentForm(forms.Form):
    name = forms.CharField(
        label='Name',
        label_suffix=':',
        max_length=25,
        help_text='Enter your correct name',
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'})
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.TextInput(attrs={'placeholder':'Enter Email'}),
        disabled=True,
    )

    pincode = forms.IntegerField(
        label='Pin code',
        min_value=100000,
        max_value=999999,
        error_messages={
            'min_value': 'Enter at least 6 digits',
            'max_value': 'Enter maximum 6 digits',
        },
        widget=forms.TextInput(attrs={'placeholder': '6 digit pincode'})
    )

    # Date-related fields
    dob = forms.DateField(
        label='Date Of Birth',
        required=False,
        help_text='Enter YYYY-MM-DD format',
        widget=forms.TextInput(attrs={'type':'date','placeholder': 'ex.1993/05/10'})
    )

    appointment_time = forms.TimeField(
        label='Appointment Time',
        required=False,
        widget=forms.TextInput(attrs={'type':'time','placeholder': 'ex.10:00'})
    )

    appointment_date = forms.DateField(
        label='Appointment Date',
        required=False,
        widget=forms.TextInput(attrs={'type':'date','placeholder': 'ex.1993/05/10'})
    )

    appointment_datetime = forms.DateTimeField(
        label='Appointment Date Time',
        required=False,
        widget=forms.TextInput(attrs={'type':'datetime-local','placeholder': 'ex.1993/05/10 10:00'})
    )

    is_agreed = forms.BooleanField(label='IsAgreed')
    agree_terms = forms.NullBooleanField(label='I Agreed')

    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female')
    ]

    INTERESTS_CHOICE = [
        ('c', 'Cricket'),
        ('f', 'Football'),
        ('r', 'Reading')
    ]

    # Choice-related fields
    gender = forms.ChoiceField(
        label='Gender',
        choices=GENDER_CHOICE)
        
                            
    

    interests = forms.MultipleChoiceField(
        label='Your Interest',
        choices=INTERESTS_CHOICE,
        widget=forms.SelectMultiple(attrs={'placeholder': 'Select Multiple Interests'})
    )

    # File and URL fields
    profile_image = forms.ImageField(
        label='Profile Pic',
        required=False,
        widget=forms.ClearableFileInput()
    )

    resume = forms.FileField(
        label='Upload Resume',
        required=False,
        widget=forms.ClearableFileInput(attrs={'placeholder': 'Upload Your Resume'})
    )

    website = forms.URLField(
        label='Personal Website',
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Enter website'})
    )

    # Other fields
    mobile_no = forms.RegexField(
        regex=r'^[6-9]\d{9}$',
        widget=forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
        error_messages={'invalid': 'Enter a valid 10-digit Indian mobile number starting with 6-9.'}
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        max_length=10,
        validators=[MinLengthValidator(3)]
    )

    slug = forms.SlugField(label='Slug',widget=forms.TextInput(attrs={'placeholder':'enter slug'}))

    ip_address = forms.GenericIPAddressField(
        label='IP Address',
        protocol='both',
        unpack_ipv4=True,
        localize=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your IPv4 or IPv6 address'})
    )

    rating = forms.DecimalField(
        label='Ratings',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter rating'})
    )

    content = forms.CharField(
        label='Post-Content',widget=forms.Textarea(attrs={'placeholder':'Enter Multiple Line of Text'})
    )

    # marriedornot=forms.RadioSelect(label='Married or Not',widget=forms.TextInput(attrs={'type':"radio"}))
    MARRIED_CHOICES = [('yes', 'Married'),('no', 'Unmarried')]

    marriedornot = forms.ChoiceField(
        label='Marital Status',
        choices=MARRIED_CHOICES,
        widget=forms.RadioSelect
    )

    # multiwidgets
    split_date_time = forms.SplitDateTimeField(
        label='Split Date and Time Field',
        widget=forms.SplitDateTimeWidget()
    )