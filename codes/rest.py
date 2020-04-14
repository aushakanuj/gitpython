import requests
import json

def getWebsite(a):
    paramsd={}
    paramsd["ml"]=a
    paramsd["max"]=5
    base=("https://api.datamuse.com/words")
    r=requests.get(base,paramsd)
    p=r.json()
    return [i["word"] for i in p]
    
a=input("Enter a word ")
print(getWebsite(a))

