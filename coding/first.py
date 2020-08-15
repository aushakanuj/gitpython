

n = int(input())
voters = input()

avote = 0
bvote = 0
hyphen = 0
prev_vote = None

for i in voters:

    if i == "-":
        hyphen += 1
    elif i == "A":
        avote += 1
        if prev_vote is None:
            avote += hyphen
            hyphen = 0
            prev_vote = None
        if prev_vote == "B":
            avote = hyphen//2
            bvote = hyphen//2
            hyphen = 0
            prev_vote = None
    else:
        bvote += 1
        if prev_vote is None:
            hyphen = 0
            prev_vote = "B"
        else:
            bvote += hyphen
            hyphen = 0
            prev_vote = "B"


if avote > bvote:
    print("A")
elif bvote > avote:
    print("B")
else:
    print("Coalition government")
