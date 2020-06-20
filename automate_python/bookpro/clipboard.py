import pyperclip
import re

phoneRegex= re.compile(r'''(
    (\d{3} | \(\d{3}\) )?
    (\s | \. | -)?
    (\d{3})
    (\s | \. | -)
    (\d{4})
    ( \s * (ext|x|ext.) \s* (\d{2,5}) )?
)''',re.VERBOSE)

emailRegex=re.compile(r'''(

    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)


text=str(pyperclip.paste())

match=[]

for groups in phoneRegex.findall(text):
    phno="-".join([groups[1],groups[3],groups[5]])

    if groups[8]!="":
        phno+= " x"+groups[8]
    match.append(phno)
    print(groups)

for groups in emailRegex.findall(text):
    match.append(groups[0])
    print(groups)

if len(match) > 0:
    pyperclip.copy('\n'.join(match)) 
    print('Copied to clipboard:') 
    print('\n'.join(match))
else:
    print('No phone numbers or email addresses found.')
