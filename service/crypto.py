# Chứa các hàm xử lý về bảo mật như mã hoá/ giải mã

import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import json

import constants

# Hàm mã hoá private key bằng password của người dùng
def encryptPrivateKey(private_key, password):
  # Lấy 16 byte đầu password đã hash làm key
  key = password[0:16]

  # Tạo một AES mode EAX với key vừa tạo
  cipher = AES.new(key, AES.MODE_EAX)
  # Mã hoá private key bằng AES
  ciphertext, tag = cipher.encrypt_and_digest(private_key)

  # Return chuỗi byte của nonce(16 bytes) + tag(16 bytes) + ciphertext
  return cipher.nonce + tag + ciphertext

# Hàm giải mã private key
def decryptPrivateKey(private_key, password):
  # Lấy 16 byte đầu password đã hash làm key
  key = password[0:16]

  # Tách private_key thành các thành phần theo số bytes
  bytes_private_key = bytes.fromhex(private_key)
  nonce = bytes_private_key[0:16]
  tag = bytes_private_key[16:32]
  ciphertext = bytes_private_key[32:]

  # Tạo lại AES đã mã hoá bằng key, nonce
  cipher = AES.new(key, AES.MODE_EAX, nonce)

  # Giải mã private key
  return cipher.decrypt_and_verify(ciphertext, tag)

# Hàm khởi tạo cặp khoá RSA cho mỗi user khi đăng ký
def generate_key(user, password):
  # Sinh khoá ngẫu nhiên
  key = RSA.generate(2048)
  private_key = key.export_key('PEM')

  # Mã hoá private key bằng AES
  private_key = encryptPrivateKey(private_key, password)
  encrypted_private_key = private_key.hex()

  # Sinh public key từ key ban đầu
  public_key = key.publickey().exportKey('PEM').hex()

  # Tạo form lưu cặp key mới
  new_keys = {
    "email": user,
    "private_key": encrypted_private_key,
    "public_key": public_key
  }

  keys = []
  # Kiểm tra trong DB có keys chưa, nếu có thì load vào biến keys, nếu không thì bỏ qua (keys = [])
  if not os.stat(constants.USER_KEY_DB_FILE).st_size == 0:
    with open(constants.USER_KEY_DB_FILE, "r") as file:
      keys = json.load(file)
      file.close()

  # Add new keys vào biến keys
  keys.append(new_keys)

  # Ghi biến keys vào DB
  with open(constants.USER_KEY_DB_FILE, "w") as file:
    json.dump(keys, file)
    file.close()



# mess_byte = message.encode('utf-8')

# rsa_public_key = RSA.importKey(public_key)
# rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
# encrypted_text = rsa_public_key.encrypt(mess_byte)

# print('your encrypted_text is : {}'.format(encrypted_text))

# rsa_private_key = RSA.importKey(private_key)
# rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
# decrypted_text = rsa_private_key.decrypt(encrypted_text)

# print('your decrypted_text is : {}'.format(decrypted_text.decode()))
