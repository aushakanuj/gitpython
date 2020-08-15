n = int(input())
string = input()

A_count = 0
B_count = 0
hyphen_count = 0

prev_vote = '-'

for i in range(len(string)):
    if (string[i] == 'A'):
        A_count += 1
        if (prev_vote != 'B'):
            A_count += hyphen_count
            hyphen_count = 0
            prev_vote = 'A'
        else:
            A_count += hyphen_count//2
            B_count += hyphen_count//2
            hyphen_count = 0
            prev_vote = 'A'

    elif (string[i] == '-'):
        hyphen_count += 1

    else:
        B_count += 1
        if (prev_vote != 'B'):
            hyphen_count = 0
            prev_vote = 'B'
        else:
            B_count += hyphen_count
            hyphen_count = 0
            prev_vote = 'B'

if (A_count > B_count):
    print('A')
elif (A_count < B_count):
    print('B')
else:
    print('Coalition government')
