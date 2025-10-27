Secure Bidirectional Messaging System
A Python-based encrypted chat framework implementing Confidentiality, Integrity, and Authentication using RSA and AES encryption.
Screenshots
1. Server Running and Receiving Secure Messages
This screenshot shows the server successfully starting, listening for connections, performing RSA–AES key exchange, and verifying incoming messages from the client.
2. Client Sending Encrypted Messages
The client establishes a secure connection with the server, exchanges public keys, generates an AES session key, and sends encrypted messages with digital signatures.
Overview
This project demonstrates the design of a secure communication system that enforces the three core principles of cybersecurity:
Confidentiality – implemented using AES-256 encryption
Integrity – ensured through RSA digital signatures
Authentication – achieved via asymmetric key exchange
The system enables encrypted, bidirectional communication between a client and a multithreaded server.
Features
RSA-based public-key exchange and AES session key encryption
Digital signatures for integrity verification
AES-GCM symmetric encryption for message confidentiality
Multithreaded socket server supporting multiple clients
Classical ciphers (Caesar, Monoalphabetic, Transposition) included for comparative learning
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
├── screenshots/
│   ├── server_output.png
│   └── client_output.png
└── README.md
Learning Outcomes
Applied the CIA triad (Confidentiality, Integrity, Authentication) in a real-world networking context
Implemented secure key management, digital signatures, and symmetric encryption
Developed a secure client–server communication system using cryptography and socket programming
Author
Disha Thakral
Bachelor of Engineering in Information Technology
University Institute of Technology, Panjab University
