Secure Bidirectional Messaging System
A Python-based encrypted chat framework implementing Confidentiality, Integrity, and Authentication using RSA and AES.

Screenshots
1. Server Running and Receiving Secure Messages
This screenshot shows the server successfully starting, listening for connections, performing RSA–AES key exchange, and verifying incoming messages from the client.
<img width="672" height="151" alt="Screenshot 2025-10-28 at 12 11 43 AM" src="https://github.com/user-attachments/assets/9c90f77d-607d-47f9-b41e-e596fdc5e742" />


Overview
This project demonstrates the design of a secure communication system that ensures the three core principles of cybersecurity:
Confidentiality – implemented using AES-256 encryption
Integrity – maintained through RSA digital signatures
Authentication – achieved via asymmetric key exchange
The system allows encrypted, bidirectional communication between a client and a multi-threaded server.

Features
>RSA-based public-key exchange and AES session key encryption
>Digital signatures for integrity verification
>AES-GCM symmetric encryption for data confidentiality
>Multithreaded socket server supporting multiple clients
>Classical ciphers (Caesar, Monoalphabetic, Transposition) included for comparative learning and understanding basic encryption methods

Tech Stack
>Python 3.10+
>Socket Programming
>RSA and AES Cryptography
>Multithreading
>Cryptography Library
