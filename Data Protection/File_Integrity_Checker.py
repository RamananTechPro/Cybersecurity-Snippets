import hashlib

def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        # Read the file in chunks to handle large files
        chunk_size = 4096
        hasher = hashlib.sha256()
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()
    
def verify_integrity(file_path, stored_hash):
    current_hash = calculate_hash(file_path)
    if current_hash == stored_hash:
        print("File integrity verified.")
    else:
        print("File integrity check failed.")
        
        
if __name__ == "__main__":
    file_path = 'example.txt'  # Path to the file
    stored_hash = '...'  # Previously stored hash
    verify_integrity(file_path, stored_hash)
