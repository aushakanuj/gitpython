import gspread
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials
import pyperclip


scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

path = "/Users/aushakanuz/Downloads/aushakanuj@gmail.com Firefox Recovery Codes.txt"
creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)

client = gspread.authorize(creds)

sheet = client.open("trial").sheet1
sheet2 = client.open("trial").get_worksheet(2)

print(client.open("trial").worksheets())

recent_value = "start"
qnum = 1
lines = 2
questions = []

print("Program has started")

while True:

    temp_val = pyperclip.paste()

    if temp_val != recent_value and (temp_val not in questions):

        try:
            sheet.insert_row([qnum, temp_val], lines)
            sheet.insert_row(["", ""], lines + 1)
            sheet.insert_row(["", ""], lines + 2)
            questions.append(temp_val)
            print("Pasted Question{}".format(qnum))
            qnum += 1
            lines += 3
        except:

            raise ValueError
