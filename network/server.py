import socket, json, threading
from crypto.rsa_utils import *
from crypto.aes_utils import *
from crypto.classical_ciphers import *

HOST, PORT = "127.0.0.1", 65432

def handle_client(conn, addr, private_key, public_key):
    print(f"🔗 Connected with {addr}")

    # Step 1: Exchange public keys
    client_pub_pem = conn.recv(4096)
    client_pub = load_public_key(client_pub_pem)
    conn.sendall(serialize_public_key(public_key))
    print("✅ Public keys exchanged.")

    # Step 2: Receive AES key
    enc_aes = conn.recv(8192)
    aes_key = rsa_decrypt(private_key, enc_aes)
    print("🔑 AES key received securely.")

    while True:
        data = conn.recv(16384)
        if not data:
            break

        packet = json.loads(data.decode())
        msg = aes_decrypt(aes_key, packet["nonce"], packet["ciphertext"])
        sig = b64d(packet["signature"])

        try:
            verify_signature(client_pub, sig, msg)
            print(f"📩 Verified message from {addr}: {msg.decode()}")
        except Exception:
            print(f"❌ Signature invalid from {addr}")

        reply = input("💬 Server reply: ").encode()
        reply_data = aes_encrypt(aes_key, reply)
        reply_sig = sign_message(private_key, reply)

        response = {
            "nonce": reply_data["nonce"],
            "ciphertext": reply_data["ciphertext"],
            "signature": b64e(reply_sig)
        }
        conn.sendall(json.dumps(response).encode())

    conn.close()

def start_server():
    private_key, public_key = generate_rsa_keys()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("🚀 Server listening on", (HOST, PORT))

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, private_key, public_key)).start()

if __name__ == "__main__":
    start_server()
