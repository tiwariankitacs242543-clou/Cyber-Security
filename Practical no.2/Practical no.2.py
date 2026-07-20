print("Ankita Tiwari \nT124 \nTYCS \nCyber Security Practical nO.2")

'''import rsa

# Generate keys
public_key, private_key = rsa.newkeys(512)

# Input message
msg = input("Enter message: ")

# Encrypt
encrypted = rsa.encrypt(msg.encode(), public_key)
print("Encrypted:", encrypted)

# Decrypt
decrypted = rsa.decrypt(encrypted, private_key).decode()
print("Decrypted:", decrypted)'''

import tkinter as tk
import rsa

public_key, private_key = rsa.newkeys(512)

def process():
    message = msg_entry.get()

    if message == "":
        output.config(text="Please enter a message.")
        return

    encrypted = rsa.encrypt(message.encode(), public_key)
    decrypted = rsa.decrypt(encrypted, private_key).decode()

    output.config(
        text=f"Encrypted:\n{encrypted}\n\nDecrypted:\n{decrypted}"
    )


root = tk.Tk()
root.title("RSA Encryption & Decryption")
root.geometry("700x500")      
root.configure(bg="lightblue")

title = tk.Label(
    root,
    text="RSA Encryption & Decryption",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title.pack(pady=20)

msg_entry = tk.Entry(root, font=("Arial", 14), width=40)
msg_entry.pack(pady=10)

encrypt_btn = tk.Button(
    root,
    text="Encrypt & Decrypt",
    font=("Arial", 12),
    command=process,
    bg="green",
    fg="white"
)
encrypt_btn.pack(pady=15)

output = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="white",
    width=75,
    height=12,
    wraplength=600,
    justify="left"
)
output.pack(pady=20)

root.mainloop()



































