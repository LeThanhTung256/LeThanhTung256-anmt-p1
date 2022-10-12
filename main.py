import os

import pages.login_page as begin
import constants

if not os.path.isfile(constants.USER_DB_FILE):
    f_users = open(constants.USER_DB_FILE, "w")
    f_users.close()

if not os.path.isfile(constants.USER_KEY_DB_FILE):
    f_keys = open(constants.USER_KEY_DB_FILE, "w")
    f_keys.close()

begin.login_page()