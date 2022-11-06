from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *
from django.contrib.auth.models import Group
from django.conf import settings


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model= Group
        fields = ('id', 'name')


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(required=True, source="groups")
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="Email already exists")], error_messages={'blank': 'Email may not be blank', 'required': 'Email is required'})
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password], error_messages={'blank': 'Password may not be blank', 'required': 'Password is required'})
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password], error_messages={'blank': 'Confirm Password may not be blank', 'required': 'Confirm Password is required'})

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2', 'first_name', 'last_name', 'allowed_views', 'role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def to_representation(self, instance):
        rep = super(RegisterSerializer, self).to_representation(instance)
        rep['role'] = instance.groups.first().name
        return rep

    def create(self, validated_data):
        validated_data['email'] = validated_data.get('email').lower()
        validated_data.pop("password2")
        users_group = Group.objects.get(id=validated_data.pop('groups'))
        instance = super(RegisterSerializer, self).create(validated_data)
        instance.set_password(validated_data.get("password"))
        users_group.user_set.add(instance)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        attrs['email'] = attrs['email'].lower()
        # Default response contains - access token and refresh token
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Add custom data you want to include in response
        data.update({
            'id': self.user.id,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'role': self.user.groups.first().name,
            'allowed_views': self.user.allowed_views,
            'first_login': self.user.first_login
        })
        return data


class MyProfileSerializer(serializers.ModelSerializer):
    """
    My profile Serializer
    """

    role = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'allowed_views', 'role')
        read_only_fields = ("email",)

    def get_role(self, obj):
        return obj.groups.first().name


class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model= Amenity
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model= Staff
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model= Class
        fields = '__all__'


class GymSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(many=True)
    amenity = AmenitySerializer(many=True)
    class Meta:
        model= Gym
        fields = ('gym_name', 'gym_hours', 'staff', 'amenity')


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model= Membership
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model= Account
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Equipment
        fields = '__all__'