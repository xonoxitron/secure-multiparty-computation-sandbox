import hashlib
from ecdsa import SigningKey, SECP256k1


def generate_key_pair():
    # Generate a private key and corresponding public key
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()
    return sk, vk


def generate_shared_secret(vk_list):
    # Derive a shared secret key from the public keys
    public_keys = [vk.to_string() for vk in vk_list]
    public_keys.sort()  # Sorting public keys for deterministic shared secret generation
    shared_secret = hashlib.sha256(b"".join(public_keys)).digest()

    # Generate a derived secret key based on the shared secret
    sk_derived = SigningKey.from_secret_exponent(
        int.from_bytes(shared_secret, "big"), curve=SECP256k1
    )
    return sk_derived


def joint_sign(vk_list, message):
    # Generate a joint signature using the shared secret key
    shared_secret_sk = generate_shared_secret(vk_list)
    signature = shared_secret_sk.sign(message.encode())
    return signature


def joint_verify(vk_list, message, signature):
    # Verify the joint signature using the derived public key
    shared_secret_vk = generate_shared_secret(vk_list).get_verifying_key()
    try:
        shared_secret_vk.verify(signature, message.encode())
        return True
    except:
        return False


""" Example usage """


# Generate key pairs for each party
sk1, vk1 = generate_key_pair()
sk2, vk2 = generate_key_pair()
sk3, vk3 = generate_key_pair()

# Share public keys with each other
vk_list = [vk1, vk2, vk3]

# Generate a joint signature from all parties
message = "Hello, world!"
signature = joint_sign(vk_list, message)

# Verify the joint signature
valid = joint_verify(vk_list, message, signature)
print("Signature is valid:", valid)
