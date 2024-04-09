import hashlib

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    password_hash = salt + password_hash
    return password_hash

def verify_password(stored_hash, provided_password):
    salt = stored_hash[:64]
    stored_hash = stored_hash[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    return password_hash == stored_hash

# Example usage:
password = "mysecretpassword"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)
is_verified = verify_password(hashed_password, password)
print("Password Verified:", is_verified)
