def mess(a):
    val=False
    while(not val):
        res=input(a)
        res=res.upper()
        if res =="Y" or res=="N":
            val=True
        else:
            print("son of a bitch")
    return res

res=mess("son of a b")
print(res)