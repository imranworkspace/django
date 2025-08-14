from django.shortcuts import render
from .serializer import StudentSerializer
from .models import StudentModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# swagger implementation
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt

# swagger decorator
@swagger_auto_schema(
    method='post',
    request_body=StudentSerializer,
    responses={201: "Created"}
)
@swagger_auto_schema(
    method='put',
    request_body=StudentSerializer,
    responses={202: "Updated"}
)
@swagger_auto_schema(
    method='patch',
    request_body=StudentSerializer,
    responses={202: "Partially Updated"}
)
@swagger_auto_schema(
    method='delete',
    request_body=None,
    responses={200: "Deleted"}
)
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@csrf_exempt
def studApiView(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            stud_id=StudentModel.objects.get(pk=pk)
            seri=StudentSerializer(stud_id)
            return Response(seri.data,status=status.HTTP_200_OK)
        else:
            stud=StudentModel.objects.all()
            seri=StudentSerializer(stud,many=True)
            return Response(seri.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        seri= StudentSerializer(data=request.data)
        if seri.is_valid():
            name = seri.validated_data['name']
            email=seri.validated_data['email']
            password=seri.validated_data['password']
            stud_create = StudentModel.objects.create(name=name,email=email,password=password)
            stud_create.save()
            return Response({'response':'student added successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response({'response':'student records not correct'},status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        if pk is not None:
            try:
                stud_update = StudentModel.objects.get(pk=pk)
            except StudentModel.DoesNotExist:
                return Response({'response':'student not found'})
            else:
                seri=StudentSerializer(stud_update,data=request.data)
                if seri.is_valid():
                    seri.save()
                    return Response({'response':'student updated'})
                else:
                    return Response(seri.errors)

    elif request.method=='PATCH':
        if pk is not None:
            try:
                stud_patch=StudentModel.objects.get(pk=pk)
            except StudentModel.DoesNotExist:
                return Response({'response':'student does not exist'},status=status.HTTP_404_NOT_FOUND)
            else:
                seri = StudentSerializer(stud_patch,data=request.data)
                if seri.is_valid():
                    seri.save()
                    return Response({'response':'patrially data updated'},status=status.HTTP_202_ACCEPTED)
    
    elif request.method=='DELETE':
        if pk is not None:
            try:
                stud_delete=StudentModel.objects.get(pk=pk)
            except StudentModel.DoesNotExist:
                return Response({'response':'student not available'},status=status.HTTP_204_NO_CONTENT)
            else:
                stud_delete.delete()
                return Response({'response':'student deleted successfully'},status=status.HTTP_200_OK)