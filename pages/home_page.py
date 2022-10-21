import PySimpleGUI as pg
import json

import service.user as userService
import service.crypto as cryptoService
import constants
from layouts.layouts import homeLayout, userSettingsLayout, changePassLayout, encryptFileLayout, decryptFileLayout

def create_home_page(user):
  home_window = pg.Window("HomePage", homeLayout).Finalize()

  def open_setting_window(user_email):
    user, err = userService.getUserByEmail(user_email)
    if err != "":
      pg.popup_error(err)
      return

    home_window.hide()
    setting_window = pg.Window("User setting", userSettingsLayout).Finalize()
    setting_window['_US_NAME_'].update(user["fullname"])
    setting_window['_US_DOB_'].update(user['date_of_birth'])
    setting_window['_US_PHONE_'].update(user['phone_number'])
    setting_window['_US_ADD_'].update(user['address'])

    while True:
      event, values = setting_window.read()
      if event == "Exit" or event == pg.WIN_CLOSED:
        break
      
      if event == "Save": 
        user = {
          "email": user_email,
          "fullname": values["_US_NAME_"],
          "date_of_birth": values["_US_DOB_"],
          "phone_number": values["_US_PHONE_"],
          "address": values["_US_ADD_"],
        }
        
        result, err = userService.updateUserInfo(user)
        if err != None:
          pg.popup_error(err)
          break

        pg.popup_ok(result)
        break
    setting_window.close()
    home_window.un_hide()
    return
  
  def open_change_password_window(user):
    home_window.hide()
    change_password_window = pg.Window("Change password", changePassLayout).Finalize()
    while True:
      event, values = change_password_window.read()
      if event == "Exit" or event == pg.WIN_CLOSED:
        break

      if event == "Save":
        oldPass = values[0]
        newPass = values[1]
        confirmPass = values[2]

        if "" in (oldPass, newPass, confirmPass):
          pg.popup_error("All fields have to fill")

        elif confirmPass != newPass:
          pg.popup_error("Confirm password must match password")
        
        else:
          form = {
          "old": oldPass,
          "new":newPass,
          "confirm": confirmPass
          }

          result, err = userService.changePassword(form, user)
          if err != None:
            pg.popup_error(err)
          else:
            pg.popup_ok(result)
            break

    change_password_window.close()
    home_window.un_hide()
    return

  def open_encrypt_window():
    home_window.hide()
    encrypt_window = pg.Window("Encrypt file", encryptFileLayout).Finalize()
    with open(constants.USER_DB_FILE, "r") as file:
      userList = json.load(file)
      file.close()
    
    users = []
    for user in userList:
      users.append(user["email"])
    encrypt_window["_RECEIVER_"].update(values = users)

    while True:
      event, values = encrypt_window.read()
      if event == pg.WIN_CLOSED or event=="Exit":
        break
      if event == "Encrypt":
        inputFile = values["_FILE_IN_"]
        receiver = values["_RECEIVER_"]
        location = values["_LOCATION_"]
        filename = values["_FILE_NAME_"]

        flat = True
        if inputFile == "":
          encrypt_window["_ERR_FILE_"].update(visible=True)
          flat = False
        else:
          encrypt_window["_ERR_FILE_"].update(visible=False)

        if receiver == "":
          encrypt_window["_ERR_REC_"].update(visible=True)
          flat = False
        else:
          encrypt_window["_ERR_REC_"].update(visible=False)

        if location == "":
          encrypt_window["_ERR_LOC_"].update(visible=True)
          flat = False
        else:
          encrypt_window["_ERR_LOC_"].update(visible=False)

        if filename == "":
          encrypt_window["_ERR_NAME_"].update(visible=True)
          flat = False
        else:
          encrypt_window["_ERR_NAME_"].update(visible=False)

        if flat == True:
          form = {
            "inputFile": inputFile,
            "receiver": receiver,
            "location": location,
            "filename": filename,
          }

          res, err = cryptoService.encryptFile(form)
          pg.popup_ok(res)
          break

    encrypt_window.close()
    home_window.un_hide()
    return

  def open_decrypt_window(user):
    home_window.hide()
    decrypt_window = pg.Window("decrypt file", decryptFileLayout).Finalize()

    while True:
      event, values = decrypt_window.read()
      if event == pg.WIN_CLOSED or event=="Exit":
        break
      if event == "Decrypt":
        inputFile = values["_FILE_IN_"]
        location = values["_LOCATION_"]
        filename = values["_FILE_NAME_"]

        flat = True
        if inputFile == "":
          decrypt_window["_ERR_FILE_"].update(visible=True)
          flat = False
        else:
          decrypt_window["_ERR_FILE_"].update(visible=False)

        if location == "":
          decrypt_window["_ERR_LOC_"].update(visible=True)
          flat = False
        else:
          decrypt_window["_ERR_LOC_"].update(visible=False)

        if filename == "":
          decrypt_window["_ERR_NAME_"].update(visible=True)
          flat = False
        else:
          decrypt_window["_ERR_NAME_"].update(visible=False)

        if flat == True:
          form = {
            "inputFile": inputFile,
            "location": location,
            "filename": filename,
          }

          res, err = cryptoService.decryptFile(form, user)
          if err == None:
            pg.popup_ok(res)
            break
          else:
            pg.popup_error(err)

    decrypt_window.close()
    home_window.un_hide()
    return

  while True:
    event, values = home_window.read()
    if event in ("Exit", pg.WIN_CLOSED):
      break

    if event == "User settings":
      open_setting_window(user)
    
    if event == "Change password":
      open_change_password_window(user)
    
    if event == "Encrypt file":
      open_encrypt_window()

    if event == "Decrypt file":
      open_decrypt_window(user)
    

