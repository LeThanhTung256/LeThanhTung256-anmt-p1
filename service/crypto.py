import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json

import constants

def generate_key(user):
  key = RSA.generate(2048)
  private_key = key.export_key('PEM')
  # còn mã hoá private key bằng AES nữa ---
  encrypted_private_key = private_key.decode()
  # ----

  public_key = key.publickey().exportKey('PEM').decode()
  new_keys = {
    "email": user,
    "private_key": encrypted_private_key,
    "public_key": public_key
  }

  keys = []

  if not os.stat(constants.USER_KEY_DB_FILE).st_size == 0:
    with open(constants.USER_KEY_DB_FILE, "r") as file:
      keys = json.load(file)
      file.close()

  keys.append(new_keys)

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
