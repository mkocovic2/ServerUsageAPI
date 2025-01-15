import hashlib
import secrets


def generate_api_key():
    return secrets.token_urlsafe(32)


def hash_api_key(org_api_key):
    org_api_key = org_api_key.encode('utf-8')
    return hashlib.sha256(org_api_key).hexdigest()


def write_env(hash_key, filename="keys.env"):
    with open(filename, "a") as f:
        f.write('API_KEY=' + hash_key)


api_key = generate_api_key()
hash_key = hash_api_key(api_key)

print("Generated Key (Save This): ", api_key)

write_env(hash_key)
