import PySimpleGUI as pg

import service.user as userService

from layouts.layouts import homeLayout, userSettingsLayout, changePassLayout, encryptFileLayout

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

  def open_encrypt_window(user):
    home_window.hide()
    encrypt_window = pg.Window("Encrypt file", encryptFileLayout).Finalize()

    while True:
      event, values = encrypt_window.read()
      if event == pg.WIN_CLOSED or event=="Exit":
        break
      if event == "Encrypt":
        print(values["_IN_"])
    
    encrypt_window.close()
    home_window.un_hide()

  while True:
    event, values = home_window.read()
    if event in ("Exit", pg.WIN_CLOSED):
      break

    if event == "User settings":
      open_setting_window(user)
    
    if event == "Change password":
      open_change_password_window(user)
    
    if event == "Encrypt file":
      open_encrypt_window(user)
    

