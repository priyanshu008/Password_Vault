
# 🔐 Password Vault (CLI-Based Secure Password Manager)

A secure, minimal, command-line password manager built with **Python** and modern **cryptography best practices**.  
This project encrypts all stored credentials using a **master password** and never stores plaintext secrets.

---

## 🚀 Features

- 🔑 Master-password–based vault encryption
- 🔒 Strong encryption using **AES-GCM**
- 🧂 Secure key derivation with **PBKDF2 + salt**
- 📁 Local encrypted storage (JSON)
- 🖥️ Simple CLI interface
- ❌ No plaintext passwords stored anywhere

---

## 🧠 How It Works (High Level)

1. User sets a **master password**
2. A cryptographic key is derived using **PBKDF2**
3. All service credentials are encrypted using **AES-GCM**
4. Encrypted data is stored in a local vault file
5. Vault can only be decrypted with the correct master password

---

## 📂 Project Structure

```

Password_Vault/
│
├── cli/
│   ├── **init**.py
│   └── main.py          # CLI entry point
│
├── core/
│   ├── **init**.py
│   ├── crypto.py        # Encryption & decryption logic
│   └── vault.py         # Vault operations
│
├── storage/
│   └── vault.json       # Encrypted password vault
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/password-vault.git
cd password-vault
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

### 🔹 Initialize Vault

Creates a new encrypted vault.

```bash
python -m cli.main init
```

### 🔹 Add Credentials

```bash
python -m cli.main add <service> <username>
```

You’ll be prompted for:

* Master password
* Service password

### 🔹 Retrieve Credentials

```bash
python -m cli.main get <service>
```

---

## 🔐 Security Details

* **Encryption**: AES-256-GCM (Authenticated Encryption)
* **Key Derivation**: PBKDF2 with random salt
* **Integrity Protection**: GCM authentication tag
* **Threat Model**:

  * Protects against offline file access
  * Prevents tampering & unauthorized decryption

⚠️ If the master password is lost, the vault **cannot be recovered**.

---

## 🧯 Error Handling

* Wrong master password → decryption fails safely
* Corrupted vault → integrity check fails
* Fresh initialization overwrites invalid vault

---

## 📌 Limitations

* No password recovery (by design)
* Local-only storage
* No clipboard integration (yet)

---

## 🔮 Future Enhancements

* Password strength checker
* Auto password generator
* Clipboard timeout
* Multi-vault support
* Hardware-backed key storage

---

## 🧑‍💻 Author

**Priyanshu Joshi**
B.Tech Cyber Security | Ethical Hacking | Cryptography
Built for learning secure systems & real-world security engineering.

---

## 📜 License

This project is licensed under the **MIT License**.

```

