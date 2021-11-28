from cryptography.fernet import Fernet
import os

SECRET_KEY = os.environ.get('FLUTTERWAVE_PUBLIC_KEY')
SECRET_KEY = bytes(SECRET_KEY.encode('utf-8'))

key = Fernet.generate_key()  # Generate a key
token = Fernet(key)  # Create a token using the key
encrypted = token.encrypt(SECRET_KEY)  # Encrypt the message
print(encrypted)  # Print the encrypted message
decrypted = token.decrypt(encrypted)  # Decrypt the message
print(decrypted)  # Print the decrypted message

# NB: keep the key secret, it is used to encrypt and decrypt messages
