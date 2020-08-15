a = {1: 2, 2: 1, 3: 2, 4: 2, 5: 2, 6: 1, 7: 2, 8: 2, 9: 2}

b = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
     6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}


x = {11: "one", 12: "two", 13: "three", 14: "four", 15: "five",
     16: "six", 17: "seven", 18: "eight", 19: "nine", 20: "zero"}

z = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
     6: "sixty", 7: "seventy", 8: "eighty", 9: "ninty"}


n = int(input())

arr = list(map(int, input().split()))

count = 0


def vowels(asd):

    a_string = asd
    lowercase = a_string.lower()
    vowel_counts = {}

    for vowel in "aeiou":

        count = lowercase.count(vowel)
        vowel_counts[vowel] = count

    counts = vowel_counts.values()
    total_vowels = sum(counts)

    return total_vowels


count = 0
for i in arr:
    temp = convert_to_words(i)
    count += vowels(temp)
    pass


c = 0
seen = []
for i in arr:

    temp = count-i

    if temp in seen:
        c += 1
        seen.remove(temp)
    else:

        seen.append(i)


ten = 0

if c//10 == 10:
    print("hundred")
elif c//10 > 10:
    print("greater 100")
else:

    if c in x.keys():

        print(x.get(c))

    else:
        temp = c//10
        rem = c % 10

        if temp == 0:

            print(b.get(rem))
        else:
            if rem == 0:
                print(z.get(rem))
            else:
                print(z.get(rem)+" "+b.get(rem))
