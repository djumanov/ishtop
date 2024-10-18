from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, user_type, password=None, **extra_fields):
        """
        Creates and returns a user with the given phone number and user type.
        """
        if not phone_number:
            raise ValueError('The phone number must be provided')
        if not user_type:
            raise ValueError('The user type must be provided')

        # Normalize phone number and other fields
        phone_number = self.normalize_phone_number(phone_number)

        # Create user with provided fields
        user = self.model(phone_number=phone_number, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Creates and returns a superuser with the given phone number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(phone_number, "Admin", password, **extra_fields)

    def normalize_phone_number(self, phone_number):
        """
        Helper function to normalize phone number, if needed.
        """
        # Optionally, implement normalization logic here
        return phone_number
