import re


checkLength=re.compile(r".{8,}")
checkLower= re.compile(r"(?=.*?[a-z])")
checkUpper= re.compile(r"[A-Z]")
checkNumber= re.compile(r"\d")
checkSpecial= re.compile(r"[!@#$%^&*()\/-_]")


print("Enter the password:")
a=input()

print(checkLength.search(a).group(),checkLower.search(a).group())

if checkLength.search(a) is None:
    print("Password is Weak")
elif checkLower.search(a) is None:
    print("Password is Weak")
elif checkUpper.search(a) is None:
    print("Password is Weak")
elif checkNumber.search(a) is None:
    print("Password is Weak")
elif checkSpecial.search(a) is None:
    print("Password is Weak")
else:
    print("Password Strong")

checkPwd=re.compile(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*()\/\_]).{8,}$")

print((checkPwd.search(a).group()))
print(type(checkPwd.search(a).group()))

if checkPwd.search(a) is None:
    print("Pwd weak")
else:
    print("Password Strong")