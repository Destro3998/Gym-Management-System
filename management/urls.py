from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('register', RegisterAPIView, basename='register-api')
router.register('my-profile', MyProfileAPIView, basename='my-profile')
router.register('manage-user', ManageUserAPIVew, basename='manage_user_api')
router.register('group-list', GroupListAPIView, basename='group-list')
router.register('amenity', AmenityAPIView, basename='amenity')
router.register('staff', StaffAPIView, basename='staff')
router.register('class', ClassAPIView, basename='class')
router.register('gym', GymAPIView, basename='gym')
router.register('membership', MembershipAPIView, basename='membership')
router.register('account', AccountAPIView, basename='account')
router.register('equipment', EquipmentAPIView, basename='equipment')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='login-api'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh-token-api'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
]
