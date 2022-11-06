from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=254, blank=True, null=True)
    allowed_views = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=254, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=254, blank=True, null=True)
    first_login = models.CharField(max_length=1, default='Y')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f'id-{self.id} email-{self.email}'


class Amenity(models.Model):
    amenity_name = models.CharField(max_length=500)
    amenity_usage_info = models.CharField(max_length=500)
    amenity_availability = models.CharField(max_length=100)


class Staff(models.Model):
    STAFF_ROLES = [
        ('Cleaner', 'Cleaner'),
        ('Receptionist', 'Receptionist'),
        ('Instructor', 'Instructor'),
    ]
    staff_name = models.CharField(max_length=500)
    staff_email = models.EmailField(unique=True, blank=False, null=False)
    staff_address = models.CharField(max_length=500)
    staff_roles = models.CharField(max_length=50, blank=True, choices=STAFF_ROLES)
    staff_hours = models.CharField(max_length=500)


class Class(models.Model):
    class_name = models.CharField(max_length=500)
    class_timeslot = models.CharField(max_length=500)
    class_availability = models.CharField(max_length=100)
    class_staffinstructor = models.CharField(max_length=500)
    staff = models.ManyToManyField(Staff)


class Gym(models.Model):
    gym_name = models.CharField(max_length=500)
    gym_hours = models.CharField(max_length=500)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)


class Membership(models.Model):
    membership_plan = models.CharField(max_length=500)
    membership_info = models.CharField(max_length=500)
    membership_price = models.CharField(max_length=500)
    membership_deal_info = models.CharField(max_length=500)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)


class Account(models.Model):
    account_type = models.CharField(max_length=500)
    account_payments = models.CharField(max_length=500)
    account_features_and_benefits = models.CharField(max_length=500)

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=500)
    equipment_usage_info = models.CharField(max_length=500)
    equipment_availability = models.CharField(max_length=500)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
