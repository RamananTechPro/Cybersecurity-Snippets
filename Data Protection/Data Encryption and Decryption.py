from cryptography.fernet import Fernet

def generate_encryption_key():
    return Fernet.generate_key()

def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

# Example usage:
encryption_key = generate_encryption_key()
data_to_protect = "Sensitive information"
encrypted_data = encrypt_data(encryption_key, data_to_protect)
print("Encrypted:", encrypted_data)
decrypted_data = decrypt_data(encryption_key, encrypted_data)
print("Decrypted:", decrypted_data)
