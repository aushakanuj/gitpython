with open("project_twitter_data.csv","r") as f:
    lines=f.readlines()
    # #positiveWords=getPositiveWords()
    # negativeWords=getNegativeWords()
    pw=0
    nw=0
    for row in lines:
        val=row.strip().split(',')
        punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@','-',"?","…"]
        a=""
        a=val[0]
        for i in punctuation_chars:
            a=(a.replace(i,""))
        a=a.lower()
        a=a.split(" ")
        print(a)
    