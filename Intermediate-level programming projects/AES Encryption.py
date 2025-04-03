""" AES Encryption:
A program utilizing the AES algorithm for encrypting and decrypting data. The user provides data, which is encrypted using a symmetric key and then decrypted using the same key. """

"""

Warning! To ensure the code works correctly, you must install the pycryptodome library.
You can do this by running the following command:

pip install pycryptodome 

"""

import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES block size (16 bytes for AES)
BLOCK_SIZE = 16

def derive_key(password: str) -> bytes:
    """Derives a 32-byte (AES-256) key from the given password using SHA256."""
    return hashlib.sha256(password.encode()).digest()

def encrypt(plaintext: str, password: str) -> str:
    """Encrypts the given plaintext using AES-256 in CBC mode."""
    key = derive_key(password)
    cipher = AES.new(key, AES.MODE_CBC)  # Generate a new random IV
    ciphertext_bytes = cipher.encrypt(pad(plaintext.encode(), BLOCK_SIZE))
    
    # Combine IV and ciphertext, then encode in Base64
    encrypted_data = base64.b64encode(cipher.iv + ciphertext_bytes).decode()
    return encrypted_data

def decrypt(encrypted_data: str, password: str) -> str:
    """Decrypts the given Base64-encoded ciphertext using AES-256 in CBC mode."""
    try:
        key = derive_key(password)
        encrypted_bytes = base64.b64decode(encrypted_data)
        
        # Extract IV and ciphertext
        iv = encrypted_bytes[:BLOCK_SIZE]
        ciphertext = encrypted_bytes[BLOCK_SIZE:]
        
        # Decrypt and remove padding
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_bytes = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)
        
        return decrypted_bytes.decode()
    except Exception as e:
        return f"Decryption failed: {str(e)}"

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nAES Encryption & Decryption")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == "1":
            password = input("Enter encryption password: ")
            plaintext = input("Enter text to encrypt: ")
            encrypted = encrypt(plaintext, password)
            print("\nEncrypted message:")
            print(encrypted)

        elif choice == "2":
            password = input("Enter decryption password: ")
            encrypted_message = input("Enter encrypted text: ")
            decrypted = decrypt(encrypted_message, password)
            print("\nDecrypted message:")
            print(decrypted)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")