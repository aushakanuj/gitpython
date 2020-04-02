placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
f=placement.strip().split()
print(f)
d={}

for i in placement:
    if i not in d:
        d[i]=0
    d[i]=d[i]+1

key=list(d.keys())
min=key[0]
for i in key:
    if d[i]<d[min]:
        min=i
min_value=i
print(d)
print(min)
