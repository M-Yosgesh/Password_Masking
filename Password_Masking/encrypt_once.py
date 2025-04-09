from cryptography.fernet import Fernet

def generate_key():
  key = Fernet.generate_key()
  with open("secret.key","wb") as f :
    f.write(key)
  print("key is successfully saved in the file")

def encrypt_password(password):
  key = open("secret.key","rb").read()
  f = Fernet(key)
  encrypted = f.encrypt(password.encode())
  print("🔐 Encrypted password to copy:")
  print(encrypted)

if __name__ == "__main__":
  generate_key()

Mysql_password = input("Enter your Mysql password : ")
encrypt_password(Mysql_password)