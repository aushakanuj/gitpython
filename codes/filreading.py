with open("../datasets/hello.txt","r") as f:

    lines = f.readlines()
    header = lines[0]
    field_names = header.strip()

    print(field_names)
    for row in lines[1:]:
        vals = row.strip().split(',')
        if vals[5]=='NA':
            print(vals)
