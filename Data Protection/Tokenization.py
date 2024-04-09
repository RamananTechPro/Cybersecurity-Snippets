import secrets

def generate_token(length=16):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

# Example usage:
token = generate_token()
print("Generated Token:", token)
