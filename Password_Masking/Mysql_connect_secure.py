import mysql.connector
from passwords_transform import get_decrypt_key

def connect_to_mysql():
  conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password = get_decrypt_key(),
  database="test" # or your own DB
  )
  print("✅ Connected to MySQL")
  conn.close()

if __name__ == "__main__":
  connect_to_mysql()