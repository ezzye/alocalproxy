from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serialize the private key to a PEM file
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Write the private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_key_pem)

# Extract the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to a PEM file
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write the public key to a file
with open("public_key.pem", "wb") as f:
    f.write(public_key_pem)

# Encrypt some data using the public key and OAEP padding
data = b"Secret message"
oaep_padder = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)
# padded_data = oaep_padder.pad(data)
# ciphertext = public_key.encrypt(
#     padded_data,
#     padding=oaep
# )

# Encrypt the data using OAEP padding
ciphertext = oaep_padder.encrypt(
    public_key,
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH)
)


# Write the ciphertext to a file
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)

# Load the ciphertext from the file
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()

# Decrypt the ciphertext using the private key and OAEP padding
# padded_plaintext = private_key.decrypt(
#     ciphertext,
#     padding=oaep
# )

# dencrypt the data using OAEP padding
padded_plaintext = oaep_padder.encrypt(
    private_key,
    ciphertext,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH)
)

# Remove the padding from the plaintext
oaep_unpadder = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)
plaintext = oaep_unpadder.unpad(padded_plaintext)

assert plaintext == data
