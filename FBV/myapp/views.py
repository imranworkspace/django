from django.shortcuts import render,redirect
from .models import StudentModel
from .serializer import StudentSerializer
from .forms import StudentForm
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
'''from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='post',
    request_body=StudentSerializer,
    responses={201: "Created"}
) 

@api_view(['GET','POST'])
def studentView(request):
    if request.method=='GET':
        student_all=StudentModel.objects.all()
        serializer = StudentSerializer(student_all,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            print('inside ')
            serializer.save()
            return Response({'response':'user created'},status=status.HTTP_201_CREATED)
'''    

def studentView(request):  
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            student=StudentModel.objects.create(name=name,email=email,password=password,created_at='',updated_at='')
            student.save()
            # After saving, redirect to the same view to clear the form
            return redirect('myform')  # replace with your actual URL name
    else:
        fm=StudentForm()
    return render(request,'reg.html',{'fm':fm})
