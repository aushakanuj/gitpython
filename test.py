with open("final.txt","w") as d:

    with open("hello.txt","r") as f:
        
        g=f.readlines()
        s=""
        for num in range(len(g)):
            if num%2==0:
                r=g[num].strip()
                s+=" "+r     

        d.write(s)