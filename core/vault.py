import json, os
from core.kdf import derive_key, generate_salt
from core.crypto.aes_gcm import encrypt, decrypt

VAULT_PATH = "storage/vault.json"

def init_vault(master_password: str):
    if os.path.exists(VAULT_PATH):
        raise Exception("Vault already exists")

    salt = generate_salt()
    key = derive_key(master_password, salt)

    encrypted = encrypt({}, key)

    vault = {
        "kdf": "argon2id",
        "algo": "aes-256-gcm",
        "salt": salt.hex(),
        **encrypted
    }

    os.makedirs("storage", exist_ok=True)
    with open(VAULT_PATH, "w") as f:
        json.dump(vault, f, indent=2)

def load_vault(master_password: str) -> dict:
    with open(VAULT_PATH, "r") as f:
        vault = json.load(f)

    salt = bytes.fromhex(vault["salt"])
    key = derive_key(master_password, salt)

    data = decrypt(vault, key)
    return data, key, vault

def add_entry(master_password: str, service: str, username: str, password: str):
    data, key, vault = load_vault(master_password)

    data[service] = {
        "username": username,
        "password": password
    }

    encrypted = encrypt(data, key)
    vault.update(encrypted)

    with open(VAULT_PATH, "w") as f:
        json.dump(vault, f, indent=2)

def get_entry(master_password: str, service: str):
    data, _, _ = load_vault(master_password)
    return data.get(service)
