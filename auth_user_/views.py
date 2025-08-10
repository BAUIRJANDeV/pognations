from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer,LoginSerializer

class RegisterApi(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginApi(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'data':serializer.validated_data,'status':status.HTTP_200_OK})
        return Response({'data':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})

class LogutApi(APIView):
    def post(self,request):
        try:
            request.user.auth_token.delete()
            return Response({'mesage': 'Siz dasturdan chiqdingiz','status':status.HTTP_200_OK})
        except Exception as e:
            return Response({'error':str(e),'staus':status.HTTP_400_BAD_REQUEST})



