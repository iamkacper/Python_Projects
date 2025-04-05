"""
Advanced GUI Application
This script uses Python’s tkinter library to create a comprehensive graphical user interface that allows users to perform multiple tasks: greeting by name, a basic calculator, text encryption/decryption using AES, a simple notepad, and a live clock.
The application demonstrates how tkinter can be used to build versatile and interactive desktop tools.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import threading



# AES Setup
BLOCK_SIZE = 16

def derive_key(password: str) -> bytes:
    return hashlib.sha256(password.encode()).digest()

def encrypt_aes(plaintext, password):
    key = derive_key(password)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), BLOCK_SIZE))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def decrypt_aes(ciphertext, password):
    try:
        key = derive_key(password)
        encrypted_data = base64.b64decode(ciphertext)
        iv = encrypted_data[:BLOCK_SIZE]
        ct = encrypted_data[BLOCK_SIZE:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), BLOCK_SIZE)
        return pt.decode()
    except Exception as e:
        return f"Error: {str(e)}"

# Main GUI
root = tk.Tk()
root.title("Advanced GUI App")
root.geometry("600x600")

# Greeting Section
tk.Label(root, text="👤 Enter your name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

def greet_user():
    name = entry_name.get()
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")
    else:
        messagebox.showwarning("Input needed", "Please enter your name.")

tk.Button(root, text="👋 Greet Me", command=greet_user).pack(pady=5)

# Calculator Section
tk.Label(root, text="🧮 Simple Calculator (a + b):").pack(pady=5)
calc_a = tk.Entry(root, width=10)
calc_a.pack()
calc_b = tk.Entry(root, width=10)
calc_b.pack()

def calculate_sum():
    try:
        result = float(calc_a.get()) + float(calc_b.get())
        messagebox.showinfo("Result", f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

tk.Button(root, text="Calculate", command=calculate_sum).pack(pady=5)

# AES Encryption Section
tk.Label(root, text="🔐 Encrypt/Decrypt Text").pack(pady=5)
entry_plaintext = tk.Entry(root, width=50)
entry_plaintext.pack(pady=2)
entry_password = tk.Entry(root, show='*', width=30)
entry_password.pack(pady=2)

def encrypt_text():
    text = entry_plaintext.get()
    pwd = entry_password.get()
    if text and pwd:
        result = encrypt_aes(text, pwd)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Input required", "Enter text and password.")

def decrypt_text():
    text = entry_plaintext.get()
    pwd = entry_password.get()
    if text and pwd:
        result = decrypt_aes(text, pwd)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Input required", "Enter encrypted text and password.")

tk.Button(root, text="Encrypt", command=encrypt_text).pack(pady=2)
tk.Button(root, text="Decrypt", command=decrypt_text).pack(pady=2)
text_result = scrolledtext.ScrolledText(root, height=4)
text_result.pack(pady=5)

# Notepad Section
tk.Label(root, text="📝 Notepad").pack(pady=5)
notepad = scrolledtext.ScrolledText(root, height=6)
notepad.pack()

# Date and Time
clock_label = tk.Label(root, text="", font=('Helvetica', 12), fg="blue")
clock_label.pack(pady=5)

def update_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clock_label.config(text="🕒 " + now)
    root.after(1000, update_time)

update_time()

# Start GUI loop
root.mainloop()