from .models import ProfileModel
from .serializer import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def profileall(request):
    if request.method=='GET':
        all=ProfileModel.objects.all()
        print(all)
        serializer=ProfileSerializer(all,many=True)
        return Response(serializer.data)