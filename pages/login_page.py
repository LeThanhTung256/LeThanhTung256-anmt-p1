# Tạo page login
# Xử lý các event trên login page
import PySimpleGUI as pg

import service.auth as auth
import layouts.layouts as layouts
import pages.register_page as register_page
import pages.home_page as home_page

# Hàm đăng nhập (mức front-end)
def login(loginForm):
  # Kiểm tra trường email và pass không bị trống
  email = loginForm[0]
  password = loginForm[1]
  if email == "":
    return -1, "Email must not be null"
  if password == "":
    return -1, "Password must not be null"

  # Call auth service login
  return auth.login(email, password)

# Tạo cửa sổ login và xử lý các sự kiện
def login_page():
  # Tạo cửa sổ loginS
  login_window = pg.Window("Sign in", layouts.loginLayout).Finalize()

  #Xử lý sự kiện
  while True:
    event, values = login_window.read()
    if event == "Exit" or event == pg.WIN_CLOSED:
      break

    if event == "Login": 
      # Call function login
      result, error = login(values)

      # Nếu có lỗi thì show lỗi
      if error != "":
        pg.popup_error("Opps!", error, font=('Any 15'))
      
      # Nếu thành công thì chuyển đến trang home page
      else:
        login_window.hide()
        pg.PopupOK("User " + result + " login successfully", font="Any 15 bold", background_color="white", text_color="green")
        home_page.create_home_page(result)
        break

    if event == "Register":
      register_page.register_page()
      break

  login_window.close()