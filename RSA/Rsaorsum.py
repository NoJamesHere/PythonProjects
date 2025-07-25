import rsa

# ✅ Step 1: Generate keys
public_key, private_key = rsa.newkeys(512)

# ✅ Step 2: Save them correctly using PKCS1 format
with open("public_key.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private_key.pem", "wb") as fp:
    fp.write(private_key.save_pkcs1("PEM"))

print("Keys generated and saved as PEM files!")

# ✅ Step 3: Load keys from PEM files
with open("public_key.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read(), format='PEM')

with open("private_key.pem", "rb") as fp:
    private_key = rsa.PrivateKey.load_pkcs1(fp.read(), format='PEM')

# ✅ Step 4: Test encryption
message = input("Enter a message to encrypt: ").encode()

encrypted = rsa.encrypt(message, public_key)
decrypted = rsa.decrypt(encrypted, private_key)

print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted.decode()}")