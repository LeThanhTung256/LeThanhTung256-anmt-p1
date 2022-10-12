import PySimpleGUI as pg

import service.auth as auth
import layouts.layouts as layouts
import pages.login_page as login_page

def register(registerForm):
  email = registerForm[0]
  full_name = registerForm[1]
  password = registerForm[5]
  confirm_password = registerForm[6]

  if email == "":
    return -1, "Email must not be null"
  if full_name == "":
    return -1, "Full name must not be null"
  if password == "":
    return -1, "Password must not be null"
  if confirm_password == "":
    return -1, "Confirm password must not be null"
  if password != confirm_password:
    return -1, "Confirm password must match password"
  
  return auth.register(registerForm)



def register_page():
  window = pg.Window("Register", layouts.signUpLayout).Finalize()
  while True:
    event, values = window.read()
    if event == "Exit" or event == pg.WIN_CLOSED:
      break

    if event == "Register":
      result, error = register(values)
      if error != "":
        pg.popup_error("Opps!", error, font=('Any 15'))
      else:
        pg.PopupOK("User " + result + " register successfully", font="Any 15 bold", background_color="white", text_color="green")
        login_page.login_page()
        break

    if event == "Login":
      login_page.login_page()
      break
  
  window.close()




