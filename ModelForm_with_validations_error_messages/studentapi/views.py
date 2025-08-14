from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.

def demo_reg(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            
            student_create=StudentModel.objects.create(name=nm,email=em,password=pw)
            student_create.save()
            return HttpResponseRedirect('/success')
    else:
        fm=StudentForm()
    return render(request,'studentapi/reg.html',{'form':fm})

def success_form(request):
    return render(request,'studentapi/success.html')