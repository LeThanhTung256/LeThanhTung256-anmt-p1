# Xử lý các yêu cầu auth:
# - Đăng nhập
# - Đăng ký

import os
import hashlib
import json
import uuid

import service.crypto as crypto
import constants

# So sánh password trong form với pass trong db
def comparePass(password, passHash):
    hashedText, salt = passHash.split(":")
    return  hashedText == hashlib.sha256(salt.encode() + password.encode('utf-8')).hexdigest()

# Đăng nhập
def login(email, password):
    users = []

    # Nếu chưa có DB, tạo DB và return err "Email has not been used"    
    if not os.path.exists(constants.DATABASE_FORDER):
        os.makedirs(constants.DATABASE_FORDER)
        return "", "Email has not been used"

    if not os.path.isfile(constants.USER_DB_FILE):
        f_users = open(constants.USER_DB_FILE, "w")
        f_users.close()
        return "", "Email has not been used"

    # Kiểm tra nếu trong DB chưa có user thì skip. Lúc đó users = [], còn k thì load data vào biến users
    if not os.stat(constants.USER_DB_FILE).st_size == 0:
        with open(constants.USER_DB_FILE, "r") as file:
            users = json.load(file)
            file.close()

    for user in users:
        # Nếu email có trong DB
        if user["email"] == email:
            if comparePass(password, user["password"]):
                # Nếu đúng password, return email, không có err
                return email, ""
            else:
                # Nếu sai password, return err
                return "", "Incorrect password! Try again"

    # Nếu không có email nào trùng khớp, return err
    return "", "Email has not been used"

# Đăng ký
def register(registerForm):
    email = registerForm[0]
    password = registerForm[5]

    users = []
    # Kiểm tra nếu trong DB chưa có user thì bỏ qua, tức là users = [], nếu có data thì load data vào biến users
    if not os.path.exists(constants.DATABASE_FORDER):
        os.makedirs(constants.DATABASE_FORDER)
    
    if not os.path.isfile(constants.USER_DB_FILE):
        f_users = open(constants.USER_DB_FILE, "w")
        f_users.close()

    if not os.stat(constants.USER_DB_FILE).st_size == 0:
        with open(constants.USER_DB_FILE, "r") as file:
            users = json.load(file)
            file.close()
        
        # Kiểm tra nếu email đã được sử dụng thì return err
        for user in users:
            if user["email"] == email:
                return "", "Email has been used"
    
    # Hash pass bằng sha256 và thêm salt
    salt = uuid.uuid4().hex
    pashHash = hashlib.sha256(salt.encode() + password.encode('utf-8')).hexdigest() + ":" + salt
    
    # Tạo user mới
    newUser = {
        "email": email,
        "fullname": registerForm[1],
        "date_of_birth": registerForm[2],
        "phone_number": registerForm[3],
        "address": registerForm[4],
        "password": pashHash
    }

    # Add user mới vào biến users
    users.append(newUser)
    # Ghi biến users vào file user db
    with open(constants.USER_DB_FILE, "w") as file:
        json.dump(users, file)
        file.close()
    
    crypto.generate_key(email, pashHash)

    return email, ""

