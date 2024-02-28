from cryptography.fernet import Fernet
import os
import customtkinter
from tkinter import filedialog 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x250")
root.title("TeCryptAlgorithm")




def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("Secret.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        try:
            decrypted_data = f.decrypt(encrypted_data)
        except InvalidToken:
            print("Invalid key")
            return
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_file():
    filename = filedialog.askopenfilename()
    if filename:
        generate_key()
        key = load_key()
        encrypt(filename, key)
        print("File Encrypted Successfully!!!")
    else:
        print("No file selected.")

def decrypt_file():
    filename = filedialog.askopenfilename()
    if filename:
        key = load_key()
        decrypt(filename, key)
        print("File Decrypted Successfully!!!")
    else:
        print("No file selected.")

label = customtkinter.CTkLabel(root, text="TeCryptAlgorithm", font=('Roboto', 24))
label.pack(pady=10, padx=10)

def encrypt_button_clicked():
    encrypt_file()

def decrypt_button_clicked():
    decrypt_file()

encrypt_button = customtkinter.CTkButton(root, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.pack(pady=12)

decrypt_button = customtkinter.CTkButton(root, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.pack(pady=12)


root.mainloop()