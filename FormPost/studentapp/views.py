from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.
def demo_form(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['email'])
            print(fm.cleaned_data['password'])
            return HttpResponseRedirect('/success')
        else:
            print('form not validated')
            
    else:
        fm=StudentForm()
    return render(request,'studentapp/reg.html',{'form':fm})

def success(request):
    return render(request,'studentapp/success.html')