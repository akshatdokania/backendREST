from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login


class UserCreate(APIView):
    permission_classes=[permissions.AllowAny]                                  #View for user registration
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, 201)
        return Response(serializer.errors, 400)

class UserLogin(APIView):
    permission_classes=[permissions.AllowAny]                                 #Login view to authenticate users
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data= serializer.data
            return Response(new_data, 200)
        return Response(serializer.errors, 400)
