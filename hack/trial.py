import gspread
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

path = "/Users/aushakanuz/Downloads/sheetconnection-286007-2ef7debc8d9c.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)

client = gspread.authorize(creds)

sheet = client.open("trial").sheet1

# print(sheet.get_all_records())

print(sheet.row_values(3))
