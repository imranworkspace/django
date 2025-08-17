from django.shortcuts import render
from rest_framework.response import Response
from .models import PostModel,AuthorModel
from .serializer import PostSerializer,AuthorSerializer
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
# swagger implementation
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt
# authentication and authorization
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# swagger decorator
@swagger_auto_schema(
    method='post',
    request_body=PostSerializer,
    responses={201: "Created"}
)
@swagger_auto_schema(
    method='put',
    request_body=PostSerializer,
    responses={202: "Fully Updated"}
)
@swagger_auto_schema(
    method='patch',
    request_body=PostSerializer,
    responses={202: "Partially Updated"}
)
@swagger_auto_schema(
    method='delete',
    request_body=None,
    responses={200: "Deleted"}
)


@api_view(['GET','POST','PUT','PATCH','DELETE'])
@csrf_exempt
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def postView(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            stud_get=PostModel.objects.get(pk=pk)
            seri=PostSerializer(stud_get)
            return Response(seri.data,status=status.HTTP_200_OK) 
        else:
            stud_all=PostModel.objects.all()
            seri=PostSerializer(stud_all,many=True)
            return Response(seri.data,status=status.HTTP_200_OK)  

    if request.method=='POST':
        seri=PostSerializer(data=request.data)
        if seri.is_valid():
            author=seri.validated_data['author']
            post_title=seri.validated_data['post_title']
            post_description=seri.validated_data['post_description']
            print(post_title)
            stud_create=PostModel.objects.create(author=author,post_title=post_title,post_description=post_description,
                                                 current_at="",updated_at="")
            stud_create.save()
            return Response({'response':'student created'},status=status.HTTP_201_CREATED)
        else:
            return Response(seri.errors,status=status.HTTP_204_NO_CONTENT)
    
    if request.method=='PUT':
        if pk is not None:
            try:
                stud_update=PostModel.objects.get(pk=pk)
            except PostModel.DoesNotExist:
                return Response({'response':'record not found'},status=status.HTTP_204_NO_CONTENT)
            else:
                seri=PostSerializer(stud_update,data=request.data)
                if seri.is_valid():
                    seri.save()
                    return Response({'reponse':'fully updated'},status=status.HTTP_200_OK)
            
    if request.method=='PATCH':
        if pk is not None:
            try:
                stud_update=PostModel.objects.get(pk=pk)
            except PostModel.DoesNotExist:
                return Response({'response':'record not found'},status=status.HTTP_204_NO_CONTENT)
            else:
                seri=PostSerializer(stud_update,data=request.data)
                if seri.is_valid():
                    seri.save()
                    return Response({'reponse':'partially updated'},status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        if pk is not None:
            try:
                stud_delete = PostModel.objects.get(pk=pk)
                stud_delete.delete()
                return Response({'response':'record deleted'},status=status.HTTP_200_OK)
            except PostModel.DoesNotExist:
                return Response({'response':'record not found'},status=status.HTTP_204_NO_CONTENT)
            