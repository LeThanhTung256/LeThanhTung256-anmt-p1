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
  [pg.T("", size = (5,0)), pg.T("", key = "_USER_NAME_", font="Any 20")],
  [pg.T("")],
  [pg.Button("User settings", size = (20, 0), font="Any 18"), pg.Button("Change password", size = (20, 0), font="Any 18")],
  [pg.Button("Encrypt file", size = (20, 0), font="Any 18"), pg.Button("Decrypt file", size = (20, 0), font="Any 18")],
  [pg.Button("Sign file", size = (20, 0), font="Any 18"), pg.Button("Confirm signature", size = (20, 0), font="Any 18")],
  [pg.T("")],
  [pg.T("", size = (50, 0)), pg.Button("Exit", size = (10, 0), font="Any 15")]
]

userSettingsLayout = [
  [pg.T("")],
  [pg.Text("Full name", size=(15, 1), font="Any 18"), pg.InputText(size=(30, 1), font="Any 15", key='_US_NAME_')],
  [pg.Text("Date of birth", size=(15, 1), font="Any 18"), pg.InputText(size=(30, 1), font="Any 15", key='_US_DOB_')],
  [pg.Text("Phone number", size=(15, 1), font="Any 18"), pg.InputText(size=(30, 1), font="Any 15", key='_US_PHONE_')],
  [pg.Text("Address", size=(15, 1), font="Any 18"), pg.InputText(size=(30, 1), font="Any 15", key='_US_ADD_')],
  [pg.T("")],
  [pg.T("", size=(60, 0)), pg.Button("Save", font="Any 15"), pg.Button("Exit", font="Any 15")]
]

changePassLayout = [
  [pg.T("")],
  [pg.Text("Old password", size=(15, 1), font="Any 18"), pg.InputText(password_char="*", size=(30, 1), font="Any 15")],
  [pg.Text("New password", size=(15, 1), font="Any 18"), pg.InputText(password_char="*", size=(30, 1), font="Any 15")],
  [pg.Text("Confirm password", size=(15, 1), font="Any 18"), pg.InputText(password_char="*", size=(30, 1), font="Any 15")],
  [pg.T("")],
  [pg.T("", size=(60, 0)), pg.Button("Save", font="Any 15"), pg.Button("Exit", font="Any 15")]
]

encryptFileLayout = [
  [pg.T("")],
  [pg.Text("Select a file", size=(15, 1), font="Any 18")],
  [pg.Input(size=(20, 0), font="Any 15", disabled=True, text_color="black"), pg.FileBrowse(key="_FILE_IN_", size=(10, 1), font="Any 15")],
  [pg.Text("Must select a file", size=(50, 0), key="_ERR_FILE_", visible=False)],
  [pg.Text("Select receiver", size=(15, 1), font="Any 18")],
  [pg.Combo([], key="_RECEIVER_", size=(30, 0), font="Any 15")],
  [pg.Text("Must select a receiver", size=(30, 0), key='_ERR_REC_', visible=False)],
  [pg.Text("Select the location for encrypted file", font="Any 18")],
  [pg.Input(change_submits=True, disabled=True, size=(20,0), font="Any 15", text_color="black"), pg.FolderBrowse(key="_LOCATION_", size=(10, 1), font="Any 15")],
  [pg.Text("Must select encrypt file's location", font="Any 18" , size=(30, 0), key='_ERR_LOC_', visible=False)],
  [pg.Text("Encrypted file's name", size=(18, 0), font="Any 18"), pg.InputText(size=(10, 0), font="Any 15", key='_FILE_NAME_')],
  [pg.Text("Must enter encrypted file's name", size=(30, 0), key='_ERR_NAME_', visible=False)],
  [pg.Text("Note: if this name don't have file extension, system will use .txt as default", size=(50, 0))],
  [pg.T("")],
  [pg.T("", size=(30, 0)), pg.Button("Encrypt", font="Any 15"), pg.Button("Exit", font="Any 15")]
]

decryptFileLayout = [
  [pg.Text("Select a file", size=(15, 1), font="Any 18")],
  [pg.Input(size=(20, 0), font="Any 15", disabled=True, text_color="black"), pg.FileBrowse(key="_FILE_IN_", size=(10, 1), font="Any 15")],
  [pg.Text("Must select a file", size=(50, 0), key="_ERR_FILE_", visible=False)],
  [pg.T("")],
  [pg.Text("Select the location for decrypted file", font="Any 18")],
  [pg.Input(change_submits=True, disabled=True, size=(20,0), font="Any 15", text_color="black"), pg.FolderBrowse(key="_LOCATION_", size=(10, 1), font="Any 15")],
  [pg.Text("Must select decrypt file's location", font="Any 18" , size=(30, 0), key='_ERR_LOC_', visible=False)],
  [pg.T("")],
  [pg.Text("Decrypted file's name", size=(18, 0), font="Any 18"), pg.InputText(size=(10, 0), font="Any 15", key='_FILE_NAME_')],
  [pg.Text("Must enter decrypted file's name", size=(30, 0), key='_ERR_NAME_', visible=False)],
  [pg.Text("Note: if this name don't have file extension, system will use .txt as default", size=(50, 0))],
  [pg.T("")],
  [pg.T("", size=(30, 0)), pg.Button("Decrypt", font="Any 15"), pg.Button("Exit", font="Any 15")]
]