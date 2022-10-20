# Tạo trang đăng ký
# Xử lý sự kiện trên trang đăng ký

import PySimpleGUI as pg

import service.auth as auth
import layouts.layouts as layouts
import pages.login_page as login_page
import pages.home_page as home_page

# Hàm đăng ký (mức front-end)
def register(registerForm):
  email = registerForm[0]
  full_name = registerForm[1]
  password = registerForm[5]
  confirm_password = registerForm[6]

  # Kiểm tra email, pass, confirmpass, full name không bị trống
  if email == "":
    return -1, "Email must not be null"
  if full_name == "":
    return -1, "Full name must not be null"
  if password == "":
    return -1, "Password must not be null"
  if confirm_password == "":
    return -1, "Confirm password must not be null"
  
  # Kiểm tra confirm password có giống với pass
  if password != confirm_password:
    return -1, "Confirm password must match password"
  
  # Call auth sevice register
  return auth.register(registerForm)

# Tạo cửa sổ đăng ký và xử lý các event
def register_page():
  # Tạo cửa sổ đăng ký
  register_window = pg.Window("Register", layouts.signUpLayout).Finalize()

  # Xử lý các event
  while True:
    event, values = register_window.read()
    if event == "Exit" or event == pg.WIN_CLOSED:
      break

    if event == "Register":
      # Đăng ký
      result, error = register(values)
      # Nếu có lỗi thì thông báo
      if error != "":
        pg.popup_error("Opps!", error, font=('Any 15'))
      else:
        # Nếu thành công chuyển đến trang home
        register_window.hide()
        pg.PopupOK("User " + result + " register successfully", font="Any 15 bold", background_color="white", text_color="green")
        home_page.create_home_page(result)
        break

    if event == "Login":
      login_page.login_page()
      break
  
  register_window.close()




