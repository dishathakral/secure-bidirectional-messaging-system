import os, base64, json, struct
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def b64e(b): return base64.b64encode(b).decode()
def b64d(s): return base64.b64decode(s.encode())

def generate_aes_key():
    return AESGCM.generate_key(bit_length=256)

def aes_encrypt(aes_key, plaintext: bytes):
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    return {"nonce": b64e(nonce), "ciphertext": b64e(ciphertext)}

def aes_decrypt(aes_key, nonce_b64, ciphertext_b64):
    aesgcm = AESGCM(aes_key)
    nonce = b64d(nonce_b64)
    ciphertext = b64d(ciphertext_b64)
    return aesgcm.decrypt(nonce, ciphertext, None)
