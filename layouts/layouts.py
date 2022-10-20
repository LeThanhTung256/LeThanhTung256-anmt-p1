# Chứa các layout cho ứng dụng
import PySimpleGUI as pg

pg.theme("DarkAmber")

loginLayout = [
  [pg.Text("Email", size=(10, 1)), pg.InputText(size=(30, 1))],
  [pg.Text("Password", size=(10, 1)), pg.InputText(password_char="*", size=(30, 1))],
  [pg.Text("")],
  [pg.Text("", size=(8,1)), pg.Button("Login", size=(20, 1))],
  [pg.Text("or", size=(40, 1), justification="center")],
  [pg.Text("", size=(3,1)), pg.Button("Register", size=(10, 1)), pg.Text("", size=(3,1)), pg.Button("Exit", size=(10, 1))]
]

signUpLayout = [
  [pg.Text("Email", size=(20, 1)), pg.InputText(size=(30, 1))],
  [pg.Text("Full name", size=(20, 1)), pg.InputText(size=(30, 1))],
  [pg.Text("Date of birth", size=(20, 1)), pg.InputText(size=(30, 1))],
  [pg.Text("Phone number", size=(20, 1)), pg.InputText(size=(30, 1))],
  [pg.Text("Address", size=(20, 1)), pg.InputText(size=(30, 1))],
  [pg.Text("Password", size=(20, 1)), pg.InputText(password_char="*", size=(30, 1))],
  [pg.Text("Confirm password", size=(20, 1)), pg.InputText(password_char="*", size=(30, 1))],
  [pg.Text("")],
  [pg.Text("", size=(13,1)), pg.Button("Register", size=(20, 1))],
  [pg.Text("or", size=(50, 1), justification="center")],
  [pg.Text("", size=(8,1)), pg.Button("Login", size=(10, 1)), pg.Text("", size=(3,1)), pg.Button("Exit", size=(10, 1))]
]

homeLayout = [
  [pg.Button("User settings"), pg.Button("Change password")],
  [pg.Button("Encrypt file"), pg.Button("Decrypt file")],
  [pg.Button("Exit")]
]

userSettingsLayout = [
  [pg.Text("Full name", size=(20, 1)), pg.InputText(size=(30, 1), key='_US_NAME_')],
  [pg.Text("Date of birth", size=(20, 1)), pg.InputText(size=(30, 1), key='_US_DOB_')],
  [pg.Text("Phone number", size=(20, 1)), pg.InputText(size=(30, 1), key='_US_PHONE_')],
  [pg.Text("Address", size=(20, 1)), pg.InputText(size=(30, 1), key='_US_ADD_')],
  [pg.Button("Save"), pg.Button("Exit")]
]

changePassLayout = [
  [pg.Text("Old password", size=(20, 1)), pg.InputText(password_char="*", size=(30, 1))],
  [pg.Text("Password", size=(20, 1)), pg.InputText(password_char="*", size=(30, 1))],
  [pg.Text("Confirm password", size=(20, 1)), pg.InputText(password_char="*", size=(30, 1))],
  [pg.Button("Save"), pg.Button("Exit")]
]

encryptFileLayout = [
  [pg.Text("Select a file:"), pg.InputText(key="_OUT_"), pg.FileBrowse(key="_IN_")],
  [],
  [pg.Text("Select receiver")],
  [pg.Button("Encrypt"), pg.Button("Exit")]
]
