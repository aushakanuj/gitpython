def double(x):
    return x,x

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

nlst=map(double,lst)
print(list(nlst))

