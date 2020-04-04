d = {'x': []}
count=0

while len(d.keys()) <= 2:
    print(len(d.keys()))
    print(d.keys())
    print('Dictionaries')
    d['x'].append('d')
    print(d['x'][0])
    count=count+1
    if count==2:
        break