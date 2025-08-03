from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
# Create your views here.
def demo_form(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            print('form validated')
            print(fm.cleaned_data)
            return HttpResponseRedirect('/success')
    else:
        fm=StudentForm()
    return render(request,'studentapp/reg.html',{'form':fm})

def success_form(request):
    return render(request,'studentapp/success.html')