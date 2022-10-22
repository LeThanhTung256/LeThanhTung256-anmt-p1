# xử lý các yêu cầu liên quan đến người dùng
# - Thay đổi thông tin cá nhân
from collections import UserList
import hashlib
import json

import service.auth as authService
import service.crypto as cryptoService
import constants

# Lấy thông tin người dùng bằng email, nếu tìm được return user Info, nếu không return err
def getUserByEmail(email):
  with open(constants.USER_DB_FILE, "r") as file:
    userList = json.load(file)
    file.close()
  
  for user in userList:
    if user["email"] == email:
      return user, ""
    
  return "", "Can't find user"

# Update thông tin người dùng
def updateUserInfo(userInfo):
  with open(constants.USER_DB_FILE, "r") as file:
    userList = json.load(file)
    file.close()

  for user in userList:
    if user["email"] == userInfo["email"]:
      user["fullname"] = userInfo["fullname"]
      user["date_of_birth"] = userInfo["date_of_birth"]
      user["phone_number"] = userInfo["phone_number"]
      user["address"] = userInfo["address"]

      with open(constants.USER_DB_FILE, "w") as file:
        json.dump(userList, file)
        file.close()
      return "Update user's infomation successfully", None

  return None, "Update user's infomation unsuccessfully"

# Change password
def changePassword(form, user_email):
  oldPassHash = None
  newPassHash = None
  # Lấy danh sách người dùng
  with open(constants.USER_DB_FILE, "r") as file:
    userList = json.load(file)
    file.close()

  # Lấy danh sách các khoá của tất cả người dùng
  with open(constants.USER_KEY_DB_FILE, "r") as file:
    userKeyList = json.load(file)
    file.close()

  # Cập nhật lại mật khẩu cho người dùng
  for user in userList:
    if user["email"] == user_email:
      oldPassHash = user["password"]
      
      # Kiểm tra xem mật khẩu cũ có đúng không, nếu có thì cập nhật lại mật khẩu cho user
      if authService.comparePass(form["old"], oldPassHash):
        hashedText, salt = oldPassHash.split(":")
        newPassHash = hashlib.sha256(salt.encode() + form["new"].encode('utf-8')).hexdigest() + ":" + salt
        user["password"] = newPassHash
      else:
        # Nếu mật khẩu cũ sai thì return err
        return None, "Incorrect old password"

  # Cập nhật lại khoá private cho người dùng 
  for user in userKeyList:
    if user["email"] == user_email:
      private_key_encrypted = user["private_key"]
      private_key = cryptoService.decryptPrivateKey(private_key_encrypted, oldPassHash)
      new_private_key = cryptoService.encryptPrivateKey(private_key, newPassHash)
      user["private_key"] = new_private_key.hex()
  
  # Lưu danh sách người dùng đã updata vào file
  with open(constants.USER_DB_FILE, "w") as file:
    json.dump(userList, file)
    file.close()

  # Lưu danh sách khoá của tất cả người dùng vào file
  with open(constants.USER_KEY_DB_FILE, "w") as file:
    json.dump(userKeyList, file)
    file.close()

  return "Update successfull", None

# Lấy thông tin người dùng (Chắc chắn lấy được)
def getUserInfo(email):
  with open(constants.USER_DB_FILE, 'r') as file:
    userList = json.load(file)
    file.close()
  
  return [user for user in userList if user["email"] == email][0]

# Lấy cặp khoá của người dùng bằng email
def getUserKeys(email):
  with open(constants.USER_KEY_DB_FILE, 'r') as file:
    userList = json.load(file)
    file.close()
  
  return [userKeys for userKeys in userList if userKeys["email"] == email][0]