from cryptography.fernet import Fernet
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Set up file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")
KEY_FILE = os.path.join(BASE_DIR, "key.key")

# Key management
def load_or_generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

# Save encrypted password
def save_data(username, password, fernet):
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

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
    
    messagebox.showinfo("Success", f"Password for '{username}' saved.")

# Decrypt and display password
def read_data(username, fernet):
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        if username not in data:
            messagebox.showinfo("Not Found", f"No password found for user '{username}'.")
            return

        encrypted_password = data[username]
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
        messagebox.showinfo("Decrypted Password", f"Password for '{username}': {decrypted_password}")

    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Load encryption key
key = load_or_generate_key()
fernet = Fernet(key)

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Manager")
root.geometry("600x400")
root.configure(bg="#ffd4ba")

label = tk.Label(root, text="Password Manager", font=("Helvetica", 28, "bold"),
                 bg="#1d0505", fg="white", anchor="s", padx=10)
label.pack(pady=20, fill="x")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

style = ttk.Style()
style.theme_use("default")  # use default to make sure styles apply

# Notebook and Tabs
style.configure("TNotebook", background="#ad8c78", borderwidth=0)
style.configure("TNotebook.Tab", background="#534237", foreground="white", padding=[10, 5])
style.map("TNotebook.Tab", background=[("selected", "#310e0e")])  # selected tab color

# Frames
style.configure("TFrame", background="#ffd4ba")

# Labels
style.configure("TLabel", background="#ffd4ba", foreground="black", font=("Helvetica", 14))

# Buttons
style.configure("TButton", background="#2e2e2e", foreground="white", font=("Helvetica", 14))
style.map("TButton",
          foreground=[("active", "white")],
          background=[("active", "#444444")])

# Entry fields
style.configure("TEntry", font=("Helvetica", 14))
# --- Encrypt Tab ---
tab_encrypt = ttk.Frame(notebook)
notebook.add(tab_encrypt, text="Encrypt")

tk.Label(tab_encrypt, text="Username", font=("Helvetica", 14)).pack(pady=5)
entry_user_enc = tk.Entry(tab_encrypt, font=("Helvetica", 14))
entry_user_enc.pack(pady=5)

tk.Label(tab_encrypt, text="Password", font=("Helvetica", 14)).pack(pady=5)
entry_pass_enc = tk.Entry(tab_encrypt, font=("Helvetica", 14), show="*")
entry_pass_enc.pack(pady=5)

tk.Button(tab_encrypt, text="Save Password", font=("Helvetica", 14), bg="#310e0e", fg="white",
          command=lambda: save_data(entry_user_enc.get(), entry_pass_enc.get(), fernet)).pack(pady=10)

# --- Decrypt Tab ---
tab_decrypt = ttk.Frame(notebook)
notebook.add(tab_decrypt, text="Decrypt")

tk.Label(tab_decrypt, text="Username", font=("Helvetica", 14)).pack(pady=5)
entry_user_dec = tk.Entry(tab_decrypt, font=("Helvetica", 14))
entry_user_dec.pack(pady=5)

tk.Button(tab_decrypt, text="Retrieve Password", font=("Helvetica", 14), bg="#2e2e2e", fg="white",
          command=lambda: read_data(entry_user_dec.get(), fernet)).pack(pady=10)

# --- Seeing all passwords tab ---
tab_view = ttk.Frame(notebook)
notebook.add(tab_view, text="View All")
def view_all_passwords():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        
        if not data:
            messagebox.showinfo("No Data", "No passwords saved.")
            return
        
        all_passwords = "\n".join([f"{user}: {fernet.decrypt(p.encode()).decode()}" for user, p in data.items()])
        messagebox.showinfo("All Passwords", all_passwords)

    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
tk.Button(tab_view, text="View All Passwords", font=("Helvetica", 14), bg="#2e2e2e", fg="white",
          command=view_all_passwords).pack(pady=10)

root.mainloop()