from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print("File encrypted successfully!")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    output_file = filename.replace(".enc", "_decrypted.txt")
    with open(output_file, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print("File decrypted successfully!")

def main():
    if not os.path.exists("secret.key"):
        generate_key()

    print("1. Encrypt File")
    print("2. Decrypt File")
    choice = input("Choose option (1/2): ")
    filename = input("Enter file name: ")

    if choice == "1":
        encrypt_file(filename)
    elif choice == "2":
        decrypt_file(filename)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
