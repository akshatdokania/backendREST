from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import UserSerializer
from .models import Userdata

class UserInput(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get(self, request):
        model = Userdata.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= 204)
        return Response(serializer.errors, 400)

class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        try:
            model= Userdata.objects.get(hospitalid = id)
        except Userdata.DoesNotExist:
            return Response('User Details Not Found', 404)
        serializer = UserSerializer(model)
        return Response(serializer.data, 200)

    def put(self, request, id):
        try:
            model, created = Userdata.objects.get_or_create(hospitalid = id)
        except Userdata.DoesNotExist:
            return Response('User Detail Not Found', 404)
        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status= 204)
        return Response(serializer.errors, 400)
