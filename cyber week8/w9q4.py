import hmac
import hashlib
import time

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization


# === HMAC (MAC using SHA256 and a shared secret) ===
def mac_simulation(secret_key, message):
    key_bytes = secret_key.encode()
    message_bytes = message.encode()
    mac = hmac.new(key_bytes, message_bytes, hashlib.sha256).hexdigest()
    return mac


# === Digital Signature (RSA with SHA256) ===
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


# === Main Comparison Simulation ===
def main():
    message = "Hello, secure world!"
    secret_key = "supersecretkey"

    print("🔐 MESSAGE:", message)
    print("🔑 SHARED SECRET (for HMAC):", secret_key)
    print("\n--- HMAC (MAC) ---")
    start_mac = time.time()
    mac = mac_simulation(secret_key, message)
    end_mac = time.time()
    print("HMAC Digest       :", mac)
    print("Time Taken        :", round(end_mac - start_mac, 6), "seconds")

    print("\n--- Digital Signature ---")
    start_keygen = time.time()
    private_key, public_key = generate_keys()
    end_keygen = time.time()

    start_sig = time.time()
    signature = sign_message(private_key, message)
    end_sig = time.time()

    start_verify = time.time()
    is_verified = verify_signature(public_key, message, signature)
    end_verify = time.time()

    print("Signature Verified:", is_verified)
    print("Signature (Hex)   :", signature.hex()[:64] + "...")
    print("Key Generation    :", round(end_keygen - start_keygen, 6), "seconds")
    print("Signing Time      :", round(end_sig - start_sig, 6), "seconds")
    print("Verification Time :", round(end_verify - start_verify, 6), "seconds")

    print("\n✅ Summary:")
    print("- HMAC is faster but requires a shared secret.")
    print("- Digital Signature is slower but provides public verification and non-repudiation.")

if __name__ == "__main__":
    main()
