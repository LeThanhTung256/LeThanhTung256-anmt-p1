import json
import constants
import pages.home_page as home
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

import service.crypto as cryService

home.create_home_page("kaka@gmail.com")
