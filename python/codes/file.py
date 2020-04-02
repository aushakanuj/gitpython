with open("../datasets/hello.txt","r") as f:
    lines=f.readlines()
    for i in lines:
        print(i.strip().split(','))
