# Joint Signature Scheme with Elliptic Curve Cryptography (ECC) for Secure Multi-Party Computation (SMPC)

This is a production-friendly Python implementation of a joint signature scheme using Elliptic Curve Cryptography (ECC) for Secure Multi-Party Computation (SMPC). The implementation utilizes the `ecdsa` library for ECC operations and the `SECP256k1` Elliptic Curve.

## Functions

### `generate_key_pair()`

This function generates a key pair consisting of a private key (`sk`) and a corresponding public key (`vk`) using the `SECP256k1` curve.

**Parameters:**

- None

**Returns:**

- `sk`: A private key generated using the `SECP256k1` curve.
- `vk`: The corresponding public key derived from the private key.

### `generate_shared_secret(vk_list)`

This function generates a shared secret by deriving a key from the given list of public keys (`vk_list`).

**Parameters:**

- `vk_list`: A list of public keys from the participating parties.

**Returns:**

- `sk_derived`: A derived secret key based on the shared secret.

### `joint_sign(sk, vk_list, message)`

This function generates a joint signature by deriving a shared secret from the given list of public keys (`vk_list`) and signing the provided `message` using the private key `sk`.

**Parameters:**

- `sk`: A private key used for joint signature generation.
- `vk_list`: A list of public keys from the participating parties.
- `message`: The message to be signed.

**Returns:**

- `signature`: The joint signature generated using the shared secret and the provided `message`.

### `joint_verify(vk_list, message, signature)`

This function verifies a joint signature by deriving a shared secret from the given list of public keys (`vk_list`) and using the derived public key to verify the provided `signature` against the `message`.

**Parameters:**

- `vk_list`: A list of public keys from the participating parties.
- `message`: The message that was signed.
- `signature`: The joint signature to be verified.

**Returns:**

- `valid`: A boolean value indicating whether the joint signature is valid (`True`) or not (`False`).

## Example Usage

```python
# Generate key pairs for each party
sk1, vk1 = generate_key_pair()
sk2, vk2 = generate_key_pair()
sk3, vk3 = generate_key_pair()

# Share public keys with each other
vk_list = [vk1, vk2, vk3]

# Generate a joint signature from all parties
message = "Hello, world!"
signature = joint_sign(sk1, vk_list, message)

# Verify the joint signature
valid = joint_verify(vk_list, message, signature)
print("Signature is valid:", valid)
```

In this example, key pairs are generated for each party using the `generate_key_pair()` function. The public keys are shared among the parties by creating a `vk_list`. Then, a joint signature is generated using the `joint_sign()` function by providing a private key, the `vk_list`, and the message to be signed. Finally, the joint signature is verified using the `joint_verify()` function by providing the `vk_list`, the message, and the signature.

Ensure that the `ecdsa` library is installed before running the code (`pip install ecdsa`).

---

With this documentation, you should have a clear understanding of the provided example and be able to utilize the joint signature scheme with ECC for Secure Multi-Party Computation in your own applications.
