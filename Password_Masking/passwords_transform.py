from cryptography.fernet import Fernet

class FakeStr(str):
  def __str__(self):
    return "******"
  def __repr__(self):
    return "******"
  
def load_key():
  return open("secret.key","rb").read()

def decrypt_password(password):
  key = load_key()
  f = Fernet(key)
  decrypted = f.decrypt(password).decode()
  return FakeStr(decrypted)

def get_decrypt_key():
  secretKey = input("Enter the Secret_key :  ")
  return decrypt_password(secretKey)
