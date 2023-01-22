from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Generate a new RSA key pair
private_key = RSA.generate(2048)
public_key = private_key.publickey()

# Create an OAEP padding object
oaep_padder = PKCS1_OAEP.new(public_key)

# Encrypt some data using the public key
plaintext = b'This is the message that we want to encrypt'
ciphertext = oaep_padder.encrypt(plaintext)

# Decrypt the ciphertext using the private key
oaep_padder = PKCS1_OAEP.new(private_key)
decrypted_plaintext = oaep_padder.decrypt(ciphertext)

# Print the original and decrypted messages
print(f'Original message: {plaintext}')
print(f'Decrypted message: {decrypted_plaintext}')
