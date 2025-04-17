from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature

# Step 1: Generate RSA Key Pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Step 2: The Document to be Signed
document = b"This is a confidential document."

# Step 3: Sign the Document using Private Key
signature = private_key.sign(
    document,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Document Signed Successfully.")

# Step 4: Verify the Signature using Public Key
def verify_signature(public_key, document, signature):
    try:
        public_key.verify(
            signature,
            document,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ Signature is valid.")
    except InvalidSignature:
        print("❌ Signature is invalid.")

# Try verifying the original document
verify_signature(public_key, document, signature)

# Try verifying a tampered document
tampered_document = b"This is a hacked document."
verify_signature(public_key, tampered_document, signature)
