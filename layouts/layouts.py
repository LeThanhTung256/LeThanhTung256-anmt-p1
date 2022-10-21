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
  [pg.Text("Select a file")],
  [pg.Input(size=(25, 0), disabled=True), pg.FileBrowse(key="_FILE_IN_")],
  [pg.Text("Must select a file",size=(30, 0), key="_ERR_FILE_", visible=False)],
  [],
  [pg.Text("Select receiver")],
  [pg.Combo([], key="_RECEIVER_", size=(30, 0))],
  [pg.Text("Must select a receiver", size=(30, 0), key='_ERR_REC_', visible=False)],
  [],
  [pg.Text("Select the location for encrypted file")],
  [pg.Input(change_submits=True, disabled=True, size=(25,0)), pg.FolderBrowse(key="_LOCATION_")],
  [pg.Text("Must select encrypt file's location" ,size=(30, 0), key='_ERR_LOC_', visible=False)],
  [],
  [pg.Text("Encrypted file's name", size=(20, 0)), pg.InputText(size=(12, 0), key='_FILE_NAME_')],
  [pg.Text("Must enter encrypted file's name", size=(30, 0), key='_ERR_NAME_', visible=False)],
  [pg.Text("Note: if this name don't have file extension, system will use .txt as defaul", size=(30, 0))],
  [],
  [pg.Button("Encrypt"), pg.Button("Exit")]
]

decryptFileLayout = [
  [pg.Text("Select a file")],
  [pg.Input(size=(25, 0), disabled=True), pg.FileBrowse(key="_FILE_IN_")],
  [pg.Text("Must select a file",size=(30, 0), key="_ERR_FILE_", visible=False)],
  [],
  [pg.Text("Select the location for encrypted file")],
  [pg.Input(change_submits=True, disabled=True, size=(25,0)), pg.FolderBrowse(key="_LOCATION_")],
  [pg.Text("Must select encrypt file's location" ,size=(30, 0), key='_ERR_LOC_', visible=False)],
  [],
  [pg.Text("Encrypted file's name", size=(20, 0)), pg.InputText(size=(12, 0), key='_FILE_NAME_')],
  [pg.Text("Must enter encrypted file's name", size=(30, 0), key='_ERR_NAME_', visible=False)],
  [pg.Text("Note: if this name don't have file extension, system will use .txt as defaul", size=(30, 0))],
  [],
  [pg.Button("Decrypt"), pg.Button("Exit")]
]