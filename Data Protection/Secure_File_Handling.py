import os

def encrypt_file(file_path, key):
    # Implement the encryption logic using the encryption key
    pass

def decrypt_file(file_path, key):
    # Implement the decryption logic using the decryption key
    pass

# Example usage:
file_to_protect = "sensitive_data.txt"
encryption_key = generate_encryption_key()
encrypt_file(file_to_protect, encryption_key)
# Later, when needed, decrypt the file using the same encryption_key:
decrypt_file(file_to_protect, encryption_key)
