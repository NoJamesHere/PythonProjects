from cryptography.fernet import Fernet
import json
import os

# Get the path to the folder where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")
KEY_FILE = os.path.join(BASE_DIR, "key.key")

# Generate or load a key
def load_or_generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

# Save encrypted data
def save_data(username, password, fernet):
    encrypted_password = fernet.encrypt(password.encode()).decode()

    try:
        with open(DATA_FILE, "r") as file:
            content = file.read().strip()
            data = json.loads(content) if content else {}
    except FileNotFoundError:
        data = {}

    data[username] = encrypted_password

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Read and decrypt data
def read_data(username, fernet):
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        if username not in data:
            print(f"No password found for user '{username}'.")
            return

        encrypted_password = data[username]
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
        print(f"Decrypted password for {username}: {decrypted_password}")

    except FileNotFoundError:
        print("No data file found.")
    except Exception as e:
        print(f"An error occurred while decrypting: {e}")

# --- MAIN PROGRAM ---
which = input("Encrypt and save Data / Read and Decrypt data? (a/b): ").lower()

key = load_or_generate_key()
fernet = Fernet(key)

if which == "a":
    user = input("What Username should the password be assigned with?: ")
    passw = input("Choose a password to encrypt and save to the file: ")
    save_data(user, passw, fernet)
    print(f"Encrypted and saved password for {user}.")
elif which == "b":
    user = input("What Username should the password be read for?: ")
    read_data(user, fernet)
else:
    print("Please choose a valid option.")