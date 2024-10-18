from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from .utilits import send_sms_code
from .serializers import PhoneNumberSerializer, ConfirmAccountSerializer


# View to initiate account creation by sending an SMS code
class CreateAccountView(generics.GenericAPIView):
    serializer_class = PhoneNumberSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone_number = serializer.validated_data['phone_number']
        user_type = serializer.validated_data['user_type']

        # Send SMS code (for now, print the code)
        code = send_sms_code(phone_number)

        # You would store the code in cache or session here
        # For demo purposes, we just return the code in the response
        return Response({
            "message": "SMS code sent successfully.",
            "phone_number": phone_number,
            "code": code  # For now, return the code in response
        }, status=status.HTTP_201_CREATED)

# View to confirm the SMS code and create the account
class ConfirmAccountView(generics.GenericAPIView):
    serializer_class = ConfirmAccountSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone_number = serializer.validated_data['phone_number']
        code = serializer.validated_data['code']
        user_type = serializer.validated_data['user_type']

        # Here you would compare the stored code (e.g., from cache) with the provided code
        stored_code = '123456'  # Example stored code, replace with actual stored code retrieval logic

        if code != stored_code:
            return Response({"error": "Invalid code."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user account if the code matches
        user = User.objects.create_user(phone_number=phone_number, user_type=user_type)
        
        return Response({"message": "Account created successfully."}, status=status.HTTP_201_CREATED)
