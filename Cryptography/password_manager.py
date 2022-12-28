from cryptography.fernet import Fernet


def get_key():
    try:
        with open("key.key", "rb") as f:
            key = f.read()
    except FileNotFoundError:
        with open("key.key", "wb") as f:
            # Generate a key in byte mode.
            # e.g: b'v0UWReoJSt13GtbWFBPNHSmoToSXnYJojmpgq7qBo18=' 
            # You should keep this key safe to be able to decrypt messages. 
            key = Fernet.generate_key()
            f.write(key)
    return key


def encrypt_message(message):
    # Encrypts message passed (only bytes).
    # Using encode() method to convert message's datatype to byte.
    # It return a “Fernet token” and has strong privacy and authenticity guarantees.
    token = fer.encrypt(message.encode())
    return token


def decrypt_message(token):
    # Decrypts a Fernet token.
    # Using decode() method to convert byte to original datatype.
    # If successfully decrypted, return the original plaintext, otherwise an exception will be raised.
    return fer.decrypt(token).decode()


# Pass the key so you can be able to decrypt messages.
key = get_key()
fer = Fernet(key)

message = "Edward"
token = encrypt_message(message)
print(decrypt_message(token))




