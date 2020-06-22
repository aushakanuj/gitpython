import re

phoneNumRegex = re.compile(r'.*',re.DOTALL) 
mo = phoneNumRegex.search('My number is 415-555-4242 \n.') 

print(mo.group())

print(r"hey")

a="anuj is good boy"
print(a.strip(""))