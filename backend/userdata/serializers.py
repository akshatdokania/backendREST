from rest_framework import serializers
from .models import Userdata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = '__all__'
