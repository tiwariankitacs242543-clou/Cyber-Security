print("Ankita Tiwari")
print("T124")
print("TYCS")
print("Cyber Security Practical No.1")
'''# Rail Fence Cipher (2 Rails)

def encrypt(text):
    rail1 = ""
    rail2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    return rail1 + rail2


def decrypt(cipher):
    mid = (len(cipher) + 1) // 2

    rail1 = cipher[:mid]
    rail2 = cipher[mid:]

    result = ""
    i = j = 0

    for k in range(len(cipher)):
        if k % 2 == 0:
            result += rail1[i]
            i += 1
        else:
            result += rail2[j]
            j += 1

    return result


print("===== Rail Fence Cipher =====")

message = input("Enter Message: ")

choice = input("Encrypt or Decrypt (E/D): ").upper()

if choice == "E":
    print("Encrypted:", encrypt(message))
elif choice == "D":
    print("Decrypted:", decrypt(message))
else:
    print("Invalid Choice")'''


from tkinter import *

def encrypt(text):
    rail1 = ""
    rail2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    return rail1 + rail2


def decrypt(cipher):
    mid = (len(cipher)+1)//2

    rail1 = cipher[:mid]
    rail2 = cipher[mid:]

    result = ""
    i = j = 0

    for k in range(len(cipher)):
        if k % 2 == 0:
            result += rail1[i]
            i += 1
        else:
            result += rail2[j]
            j += 1

    return result


def encrypt_message():
    msg = entry.get()
    result_label.config(text="Encrypted: " + encrypt(msg))


def decrypt_message():
    msg = entry.get()
    result_label.config(text="Decrypted: " + decrypt(msg))


root = Tk()
root.title("Rail Fence Cipher")

Label(root, text="Enter Message").pack()

entry = Entry(root, width=40)
entry.pack()

Button(root, text="Encrypt", command=encrypt_message).pack(pady=5)

Button(root, text="Decrypt", command=decrypt_message).pack(pady=5)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
