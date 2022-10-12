import PySimpleGUI as pg

import service.auth as auth
import layouts.layouts as layouts
import pages.register_page as register_page

def login(loginForm):
  # Kiểm tra trường email và pass không bị trống
  email = loginForm[0]
  password = loginForm[1]
  if email == "":
    return -1, "Email must not be null"
  if password == "":
    return -1, "Password must not be null"

  return auth.login(email, password)

def login_page():
  window = pg.Window("Sign in", layouts.loginLayout).Finalize()
  while True:
    event, values = window.read()
    if event == "Exit" or event == pg.WIN_CLOSED:
      break

    if event == "Login": 
      result, error = login(values)
      if error != "":
        pg.popup_error("Opps!", error, font=('Any 15'))
      else:
        pg.PopupOK("User " + result + " login successfully", font="Any 15 bold", background_color="white", text_color="green")
        break

    if event == "Register":
      register_page.register_page()
      break

  window.close()