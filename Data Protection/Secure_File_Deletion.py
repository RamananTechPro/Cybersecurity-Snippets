import os
import random

def secure_delete(file_path, passes=3):
    with open(file_path, 'rb+') as f:
        file_size = os.path.getsize(file_path)
        for _ in range(passes):
            f.seek(0)
            f.write(bytearray(random.getrandbits(8) for _ in range(file_size)))
        f.truncate(0)
        
if __name__ == "__main__":
    file_path = 'example.txt'  # Path to the file
    secure_delete(file_path)
    print(f"File '{file_path}' securely deleted.")
