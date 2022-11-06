from datetime import datetime

from rest_framework import (
    permissions,
    viewsets,
    status
)
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .models import *
from .serializers import *

from .permissions import (
    UpdateOwnProfile
)
from rest_framework.exceptions import APIException
from django.contrib.auth.models import Group


class RegisterAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    http_method_names = ['post']


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class MyProfileAPIView(viewsets.ModelViewSet):
    """
    It is used for get My profile and update profile details.
    """
    permission_classes = [UpdateOwnProfile]
    serializer_class = MyProfileSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'put']


class ChangePasswordAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = User.objects.filter(email=request.user.email).first()
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")
        if user.check_password(old_password):
            if new_password == confirm_password:
                user.first_login = 'N'
                user.set_password(new_password)
                user.save()
            else:
                raise Exception('Both passwords do not match')
        else:
            raise APIException("The Old Password entered was incorrect")
        return Response({'message': 'Password changed successfully'})


class ForgotPasswordAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = User.objects.filter(email=request.data.get('email')).first()
        if user:
        # to generate a password without any number.
            random_password = User.objects.make_random_password(length=16, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789$#%^&*')
            user.first_login = 'Y'
            user.set_password(random_password)
            user.save()
        return Response({'message': 'Something went wrong. Please try again.'})


class ManageUserAPIVew(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = RegisterSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset

    def update(self, request, pk):
        user_obj = User.objects.filter(id=pk).first()
        if request.data.get('email') != user_obj.email:
            raise Exception(detail='Email cannot be changed!')
        else:
            user_obj.first_name = request.data.get('first_name')
            user_obj.last_name = request.data.get('last_name')
            user_obj.allowed_views = request.data.get('allowed_views')
            user_obj.updated_at = datetime.now()
            user_obj.updated_by = request.user.email
            #check if the user role(group) has changed then assign new role.
            if not user_obj.groups.filter(id=request.data.get('role')).exists():
                new_role = Group.objects.get(id=request.data.get('role'))
                # clear all the groups and then assign new group
                user_obj.groups.clear()
                user_obj.groups.add(new_role)
                #add entry in audit user table
            user_obj.save()
            return Response({'detail': 'Updated'})

    def destroy(self, request, pk):
        if User.objects.filter(groups__name='Admin').count() > 1 and request.user.groups.first().name == "Admin":
            user_object = self.get_object()
            user_object.deleted_at = datetime.now()
            user_object.deleted_by = request.user.email
            user_object.save()
            user_object.delete()
            return Response({'message':'User Deleted Successfully'})
        return Response({'message':'Not allowed to perform this action'})

class GroupListAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = Group.objects.all().order_by('id')
    http_method_names = ['get']


class AmenityAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AmenitySerializer
    queryset = Amenity.objects.all().order_by('id')


class StaffAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all().order_by('id')


class ClassAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClassSerializer
    queryset = Class.objects.all().order_by('id')


class GymAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GymSerializer
    queryset = Gym.objects.all().order_by('id')


class MembershipAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all().order_by('id')


class AccountAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all().order_by('id')


class EquipmentAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all().order_by('id')