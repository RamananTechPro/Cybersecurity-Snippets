import pyotp

def generate_secret_key():
    return pyotp.random_base32()

def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

def verify_otp(secret_key, otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp)

if __name__ == "__main__":
    secret_key = generate_secret_key()
    otp = generate_otp(secret_key)
    print(f"Generated OTP: {otp}")

    # Simulate user input
    user_input_otp = input("Enter OTP: ")
    if verify_otp(secret_key, user_input_otp):
        print("OTP verified. Access granted.")
    else:
        print("OTP verification failed. Access denied.")

