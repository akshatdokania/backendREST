from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q

class UserSerializer(serializers.ModelSerializer):                              #serializer for registration
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer): #serializer for login checks
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
        "password" : {"write_only": True}
        }

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password')
        if not username:
            raise ValidationError('Username and Email should be provided')
        user = User.objects.filter(
        Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('Username or Email Invalid')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Wrond email or password')
        return data
