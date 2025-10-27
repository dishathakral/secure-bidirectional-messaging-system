Secure Bidirectional Messaging System
A Python-based encrypted chat framework implementing Confidentiality, Integrity, and Authentication using RSA and AES encryption.
Overview
This project demonstrates the design of a secure communication system that ensures:
Confidentiality – using AES-256 encryption
Integrity – using RSA digital signatures
Authentication – via asymmetric key exchange
The system allows bidirectional, encrypted communication between a client and a multi-threaded server.
Features
RSA-based public-key exchange and AES session key encryption
Digital signatures for integrity verification
AES-GCM symmetric encryption for confidentiality
Multithreaded socket server supporting multiple clients
Classical ciphers (Caesar, Monoalphabetic, Transposition) for comparative learning
Tech Stack
Python 3.10+
Socket Programming
RSA and AES Cryptography
Multithreading
cryptography and sympy libraries
How to Run
# 1. Install dependencies
pip install cryptography sympy

# 2. Start the server
python -m network.server

# 3. Start the client
python -m network.client
Directory Structure
secure_messaging_system/
├── crypto/
│   ├── rsa_utils.py
│   ├── aes_utils.py
│   └── classical_ciphers.py
├── network/
│   ├── server.py
│   └── client.py
└── README.md
Learning Outcomes
Implemented the CIA triad (Confidentiality, Integrity, Authentication) in a practical networking context
Understood key management, digital signatures, and symmetric encryption
Built a secure networked system following modern cybersecurity practices
Author
Disha Thakral
B.E. Information Technology
Panjab University
