print("ANKITA TIWARI")
print("TYCS")
print("T124")
print("Cyber Security Practical No.3")

from tkinter import *
import hmac
import hashlib

key = b"secretkey"
mac = ""

def generate():
    global mac
    message = e1.get()
    mac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    l4.config(text=mac)

def verify():
    check = e2.get()
    new_mac = hmac.new(key, check.encode(), hashlib.sha256).hexdigest()

    if mac == new_mac:
        l5.config(text="MAC Verified!")
    else:
        l5.config(text="Verification Failed!")

root = Tk()
root.title("MAC")
root.geometry("400x300")

Label(root, text="Enter Message").pack()
e1 = Entry(root, width=40)
e1.pack()

Button(root, text="Generate MAC", command=generate).pack(pady=5)

Label(root, text="Generated MAC").pack()
l4 = Label(root, text="")
l4.pack()

Label(root, text="Enter Message to Verify").pack()
e2 = Entry(root, width=40)
e2.pack()

Button(root, text="Verify", command=verify).pack(pady=5)

l5 = Label(root, text="")
l5.pack()

root.mainloop()
