# Xử lý các yêu cầu auth:
# - Đăng nhập
# - Đăng ký

import os
import hashlib
import json
import uuid

import service.crypto as crypto
import constants

def comparePass(password, passHash):
    hashedText, salt = passHash.split(":")
    return  hashedText == hashlib.sha256(salt.encode() + password.encode('utf-8')).hexdigest()

def login(email, password):
    users = []
    if os.stat(constants.USER_DB_FILE).st_size == 0:
        return "", "Email has not been used"

    with open(constants.USER_DB_FILE, "r") as file:
        users = json.load(file)
        file.close()
    for user in users:
        if user["email"] == email:
            if comparePass(password, user["password"]):
                return email, ""
            else:
                return "", "Incorrect password! Try again"

    return "", "Email has not been used"
    
def register(registerForm):
    email = registerForm[0]
    password = registerForm[5]

    users = []
    if not os.stat(constants.USER_DB_FILE).st_size == 0:
        with open(constants.USER_DB_FILE, "r") as file:
            users = json.load(file)
            file.close()
        for user in users:
            if user["email"] == email:
                return "", "Email has been used"
    
    salt = uuid.uuid4().hex
    pashHash = hashlib.sha256(salt.encode() + password.encode('utf-8')).hexdigest() + ":" + salt
    
    newUser = {
        "email": email,
        "fullname": registerForm[1],
        "date_of_birth": registerForm[2],
        "phone_number": registerForm[3],
        "address": registerForm[4],
        "password": pashHash
    }

    users.append(newUser)
    with open(constants.USER_DB_FILE, "w") as file:
        json.dump(users, file)
        file.close()
    
    crypto.generate_key(email)

    return email, ""

