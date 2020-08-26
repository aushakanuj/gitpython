

def monotonous(n):

    n = list(n)
    flag = None
    count = 0
    prev = n[0]
    for i in n[1:]:
        temp = ord(i) - ord(prev)
        if temp == 0:
            prev = i
        elif temp < 0:
            if flag is None:
                flag = False
                prev = i
            elif flag:
                prev = i
                flag = None
                count += 1
            else:
                prev = i

        else:
            if flag is None:
                flag = True
                prev = i
            elif flag is False:
                prev = i
                flag = None
                count += 1

            else:
                prev = i

    if flag is None:
        return count + 1
    else:
        return count + 1


print(monotonous("cadhfbbacf"))
