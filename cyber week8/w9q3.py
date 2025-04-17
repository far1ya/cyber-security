import hmac
import hashlib

def generate_hmac(key, message, hash_func=hashlib.sha256):
    # Encode key and message to bytes
    key_bytes = key.encode('utf-8')
    message_bytes = message.encode('utf-8')

    # Create HMAC object and compute digest
    hmac_obj = hmac.new(key_bytes, message_bytes, hash_func)
    hmac_digest = hmac_obj.hexdigest()

    return hmac_digest

# Example usage
if __name__ == "__main__":
    secret_key = "supersecretkey"
    message = "This is a secure message."

    print("Message:    ", message)
    print("Secret Key: ", secret_key)

    # Generate HMAC using SHA256
    hmac_value = generate_hmac(secret_key, message)
    print("HMAC (SHA256):", hmac_value)
