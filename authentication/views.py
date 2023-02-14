from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class VerifyTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.data.get('token') or request.headers.get('Authorization').split(' ')[1]
        # If token is in the request body, use the line above instead of the one below
        # token = request.data.get('token')
        serializer = TokenVerifySerializer(data={'token': token})
        try:
            serializer.is_valid(raise_exception=True)
            return Response({'valid': True})
        except:
            return Response({'valid': False})