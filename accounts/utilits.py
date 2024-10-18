import random

def send_sms_code(phone_number):
    code = random.randint(100000, 999999)  # Generate a 6-digit code
    print(f"SMS code for {phone_number}: {code}")  # Placeholder for actual SMS sending
    return code
