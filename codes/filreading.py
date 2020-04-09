with open("../datasets/hello.txt","r") as f:
    
    lines = f.readlines()
    # header = lines[0]
    # field_names = header.strip()
    # for row in lines:
    #     vals = row.strip().split(',')
    #     if vals[5]=='NA':
    #         print(vals)
    print(lines)
