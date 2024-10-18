from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator

from .managers import UserManager


class User(AbstractBaseUser):
    APPLICANT = "Applicant"
    EMPLOYER = "Employer"
    ADMIN = "Admin"

    USER_TYPE_CHOICES = (
        (APPLICANT, 'Applicant'),
        (EMPLOYER, 'Employer'),
        (ADMIN, 'Admin'),
    )

    phone_number = models.IntegerField(unique=True, validators=[RegexValidator(r'^\d{9}$', 'Phone number must be exactly 9 digits.')])
    user_type = models.CharField(max_length=9, choices=USER_TYPE_CHOICES)
    email = models.EmailField(blank=True, null=True)
    telegram_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    telegram_username = models.CharField(max_length=128, unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def set_password(self, raw_password):
        pass

    def check_password(self, raw_password):
        return False

    def __str__(self):
        return str(self.phone_number)
