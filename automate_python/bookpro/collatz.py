
def collatz(number):
    if number==1:
        return

    if number%2==0:
        print(number//2)
        return collatz(number//2)

    else:
        print(number*3+1)
        return collatz(3*number+1)

print("Enter a number")

a=int(input())

collatz(a)

