from rest_framework import serializers
from .models import User


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=9)
    user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 9:
            raise serializers.ValidationError("Phone number must be exactly 9 digits.")
        return value

class ConfirmAccountSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=9)
    code = serializers.CharField(max_length=6)
    user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 9:
            raise serializers.ValidationError("Phone number must be exactly 9 digits.")
        return value

    def validate_code(self, value):
        if len(value) != 6 or not value.isdigit():
            raise serializers.ValidationError("Code must be a 6-digit number.")
        return value
