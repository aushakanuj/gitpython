import re
print("Hello world")
phoneNumRegex = re.compile(r'.*',re.DOTALL) 
mo = phoneNumRegex.search('My number is 415-555-4242 \n.') 

