
from  rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
class RegisterApi(APIView):
    def post(self,request):
        serializer=RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        return Response(serializer.errors)
# Create your views here.
