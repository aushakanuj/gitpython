
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
d=dictionary
sorted_values=sorted(d,reverse=True,key=lambda x:d[x])
print(sorted_values)
