# Chứa các hàm xử lý về bảo mật như mã hoá/ giải mã

from fileinput import filename
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import json

import service.user as userService
import constants

# Hàm mã hoá private key bằng password của người dùng
def encryptPrivateKey(private_key, password):
  hashedPass, salt = password.split(":")
  # Lấy 16 byte đầu password đã hash làm key
  key = bytes.fromhex(hashedPass)[0:16]

  # Tạo một AES mode EAX với key vừa tạo
  cipher = AES.new(key, AES.MODE_EAX)
  # Mã hoá private key bằng AES
  ciphertext, tag = cipher.encrypt_and_digest(private_key)

  # Return chuỗi byte của nonce(16 bytes) + tag(16 bytes) + ciphertext
  return cipher.nonce + tag + ciphertext

# Hàm giải mã private key
def decryptPrivateKey(private_key, password):
  hashedPass, salt = password.split(":")
  # Lấy 16 byte đầu password đã hash làm key
  key = bytes.fromhex(hashedPass)[0:16]

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
  if not os.path.isfile(constants.USER_KEY_DB_FILE):
    f_keys = open(constants.USER_KEY_DB_FILE, "w")
    f_keys.close()

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

# Hàm mã hoá khoá session bằng RSA |  | input:(bytes: sessionKey, string: email) --> output(bytes: encryptedKey)
def encryptSessionKey(sessionKey, userEmail):
  userKeys = userService.getUserKeys(userEmail)

  publicKey = bytes.fromhex(userKeys['public_key'])
  rsaPublicKey = RSA.importKey(publicKey)
  rsaPublicKey = PKCS1_OAEP.new(rsaPublicKey)
  encryptedKey = rsaPublicKey.encrypt(sessionKey)

  return encryptedKey

# Hàm giải mã khoá session bằng RSA | | input:(bytes: encryptedKey, string: email) --> output(bytes: sessionKey)
def decryptSessionKey(encryptKey, userEmail):
  userInfo = userService.getUserInfo(userEmail)
  userKeys = userService.getUserKeys(userEmail)

  encryptedPrivateKey = userKeys["private_key"]
  privateKey = decryptPrivateKey(encryptedPrivateKey, userInfo["password"])
  rsaPrivateKey = RSA.importKey(privateKey)
  rsaPrivateKey = PKCS1_OAEP.new(rsaPrivateKey)
  sessionKey = rsaPrivateKey.decrypt(encryptKey)

  return sessionKey

# Hàm mã hoá một file bằng thuật toán AES. Ksession sinh nhẫu nhiên, sau đó được mã hoá bằng RSA với key pair của người nhận
# Đầu vào là một form chứa input file, receiver, location và file name của file kết quả
def encryptFile(form):
  # Đọc file đầu vào theo byte
  inputFile = form["inputFile"]
  with open(inputFile, 'rb') as file:
    data = file.read()

  # Đặt file đầu ra
  outputFile = form["location"] + '/' + form["filename"]
  fileName = form["filename"].split('.')
  if len(fileName) == 1:
    outputFile += ".txt"

  # Tạo key session (16 bytes)
  sessionKey = get_random_bytes(16)
  # Tạo mã hoá AES
  cipher = AES.new(sessionKey, AES.MODE_EAX)
  # Mã hoá data bằng AES
  encryptedData, tag = cipher.encrypt_and_digest(data)

  # Mã hoá sessionKey
  encryptedSessionKey = encryptSessionKey(sessionKey, form["receiver"])

  # Cần lưu sessionKey, nonce, tag, encryptedData vào file output
  # Tuy nhiên để có thế giải mã được cần phải trích xuất các thành phần ra. Do đó em ngăn cách các phần bằng một chuỗi ký tự đặc trưng là: "18120640-LeThanhTung" + email người nhận:
  text = ("18120640-LeThanhTung" + form["receiver"]).encode()
  output = encryptedSessionKey + text + cipher.nonce + text + tag + text + encryptedData
  
  # Ghi kết quả vào file output
  with open(outputFile, "wb") as file:
    file.write(output)
    file.close() 

  res, err = "Crypt successfull", None
  return res, err

# Hàm giải mã một file bằng thuật toán AES
# Đầu vào là một form chứa input file, location và file name của file kết quả
def decryptFile(form, userEmail):
  # Đọc file đầu vào theo byte
  inputFile = form["inputFile"]
  with open(inputFile, 'rb') as file:
    data = file.read()

  # Đặt file đầu ra
  outputFile = form["location"] + '/' + form["filename"]
  fileName = form["filename"].split('.')
  if len(fileName) == 1:
    outputFile += ".txt"

  # Tách các thành phần trong data
  text = ("18120640-LeThanhTung" + userEmail).encode()
  item = data.split(text)
  if len(item) < 4:
    return None, "You are not allowed to decrypt this file"

  enyptedSessionKey = item[0]
  nonce = item[1]
  tag = item[2]
  encryptedData = item[3]

  # Giải mã session key
  sessionKey = decryptSessionKey(enyptedSessionKey, userEmail)

  # Tạo lại AES
  cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)

  # Giải mã nội dung file
  decryptedData = cipher.decrypt_and_verify(encryptedData, tag)

  # Ghi nội dung vào file kết quả
  with open(outputFile, "wb") as file:
    file.write(decryptedData)
    file.close()

  res, err = "Decrypt file complete", None
  return res, err
