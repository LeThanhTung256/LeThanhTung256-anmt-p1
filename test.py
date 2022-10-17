from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES


import constants
import json

with open(constants.USER_DB_FILE, "r") as file:
  data = json.load(file)
  file.close()

for x in data:
  if x["email"] == "ccl@gmail.com":
    item = x
    break

hashedText, salt = x["password"].split(":")
key = hashedText[0:16].encode("utf-8")
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(b'conchotung')
pr = cipher.nonce + tag + ciphertext
pr1 = pr.hex()
print(cipher.nonce)
# with open("./test.json", "w") as file:
#   json.dump(pr, file)
#   file.close()

pr2 = bytes.fromhex(pr1)
nonce = pr2[0:16]
tag1 = pr2[16:32]
text = pr2[32:]

print(nonce)

cipher1 = AES.new(key, AES.MODE_EAX, nonce)
detext = cipher1.decrypt_and_verify(text, tag1)


print(detext)




