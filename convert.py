from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64
import json
import hashlib

def base64url_uint(val: int) -> str:
    byte_val = val.to_bytes((val.bit_length() + 7) // 8, byteorder="big")
    return base64.urlsafe_b64encode(byte_val).rstrip(b"=").decode("ascii")

def sha256_thumbprint(jwk_dict: dict) -> str:
    # Create canonical JWK for thumbprint (only e, kty, n)
    thumbprint_dict = {
        "e": jwk_dict["e"],
        "kty": jwk_dict["kty"],
        "n": jwk_dict["n"]
    }
    thumbprint_json = json.dumps(thumbprint_dict, separators=(",", ":"), sort_keys=True)
    thumbprint_bytes = thumbprint_json.encode("utf-8")
    digest = hashlib.sha256(thumbprint_bytes).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")

# Load certificate
with open("cert.crt", "rb") as f:
    cert_data = f.read()

# Load and parse certificate
cert = x509.load_pem_x509_certificate(cert_data, backend=default_backend())
public_key = cert.public_key()

if not isinstance(public_key, rsa.RSAPublicKey):
    raise ValueError("Certificate does not contain an RSA public key.")

numbers = public_key.public_numbers()
n = base64url_uint(numbers.n)
e = base64url_uint(numbers.e)

# Build JWK
jwk = {
    "kty": "RSA",
    "alg": "RS256",
    "use": "sig",
    "n": n,
    "e": e
}

# Add 'kid'
jwk["kid"] = sha256_thumbprint(jwk)

# Output the JWK
print(json.dumps(jwk, indent=2))
