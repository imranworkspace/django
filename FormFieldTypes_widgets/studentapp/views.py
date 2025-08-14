from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def demo_form(request):
    fm=StudentForm()
    return render(request,'index.html',{'form':fm})