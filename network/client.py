import socket, json
from crypto.rsa_utils import *
from crypto.aes_utils import *

HOST, PORT = "127.0.0.1", 65432

def start_client():
    priv, pub = generate_rsa_keys()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Step 1: Exchange public keys
    s.sendall(serialize_public_key(pub))
    server_pub_pem = s.recv(4096)
    server_pub = load_public_key(server_pub_pem)
    print("✅ Public keys exchanged.")

    # Step 2: Send AES key
    aes_key = generate_aes_key()
    enc_aes = rsa_encrypt(server_pub, aes_key)
    s.sendall(enc_aes)
    print("🔑 AES key sent securely.")

    while True:
        msg = input("💬 Client message: ").encode()
        msg_data = aes_encrypt(aes_key, msg)
        sig = sign_message(priv, msg)

        packet = {
            "nonce": msg_data["nonce"],
            "ciphertext": msg_data["ciphertext"],
            "signature": b64e(sig)
        }
        s.sendall(json.dumps(packet).encode())

        # Receive reply
        data = s.recv(16384)
        if not data:
            break
        resp = json.loads(data.decode())

        reply = aes_decrypt(aes_key, resp["nonce"], resp["ciphertext"])
        sig2 = b64d(resp["signature"])

        try:
            verify_signature(server_pub, sig2, reply)
            print("✔ Server verified:", reply.decode())
        except Exception:
            print("❌ Signature verification failed!")

if __name__ == "__main__":
    start_client()
