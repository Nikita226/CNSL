from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_key():
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=256,
        backend=default_backend()
    )
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_key

def encrypt_message(message, key):
    private_key = serialization.load_pem_private_key(key, password=None, backend=default_backend())
    public_key = private_key.public_key()
    serialized_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()

    cipher = public_key.encrypt(
        padded_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256),
            algorithm=hashes.SHA256,
            label=None
        )
    )

    return cipher, serialized_public_key

def decrypt_message(cipher, key):
    private_key = serialization.load_pem_private_key(key, password=None, backend=default_backend())
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_data = private_key.decrypt(
        cipher,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256),
            algorithm=hashes.SHA256,
            label=None
        )
    )

    message = unpadder.update(decrypted_data) + unpadder.finalize()
    return message

if __name__ == "__main":
    message = b"This is a secret message"

    # Generate a private key
    private_key = generate_key()

    # Encrypt the message with the public key
    cipher, serialized_public_key = encrypt_message(message, private_key)

    # Decrypt the message with the private key
    decrypted_message = decrypt_message(cipher, private_key)

    print("Original Message:", message)
    print("Decrypted Message:", decrypted_message)
