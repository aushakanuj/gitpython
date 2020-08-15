def getPositiveWords():
    positiveWords = []
    with open("positive_words.txt", 'r') as p:
        lines = p.readlines()
        for word in lines:
            if word[0] != ";" and word[0] != "\n":
                positiveWords.append(word.strip())
    p.close()
    return positiveWords


def getNegativeWords():
    negativeWords = []
    with open("negative_words.txt", 'r') as p:
        lines = p.readlines()
        for word in lines:
            if word[0] != ";" and word[0] != "\n":
                negativeWords.append(word[0].strip())
    p.close()
    return negativeWords


with open("test.csv", "w") as w:
    with open("project_twitter_data.csv", "r") as f:

        lines = f.readlines()
        positiveWords = getPositiveWords()
        negativeWords = getNegativeWords()
        header = lines[0].strip().split(",")
        w.write("{},{},{},{}\n".format(header[1], header[2], "Positive count", "Negative count"))
        for row in lines[1:]:
            pw = 0
            nw = 0
            val = row.strip().split(',')
            punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
            a = ""
            a = val[0]
            for i in punctuation_chars:
                a = (a.replace(i, ""))
            a = a.lower()
            a = a.split(" ")
            for i in a:
                if i in positiveWords:
                    pw = pw+1
                if i in negativeWords:
                    nw = nw+1
            w.write("{},{},{},{} \n".format(val[1], val[2], pw, nw))
    f.close()
w.close()
