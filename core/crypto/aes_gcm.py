from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, json

def encrypt(data: dict, key: bytes) -> dict:
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(nonce, json.dumps(data).encode(), None)

    return {
        "nonce": nonce.hex(),
        "ciphertext": ciphertext.hex()
    }

def decrypt(payload: dict, key: bytes) -> dict:
    aes = AESGCM(key)
    plaintext = aes.decrypt(
        bytes.fromhex(payload["nonce"]),
        bytes.fromhex(payload["ciphertext"]),
        None
    )
    return json.loads(plaintext)
