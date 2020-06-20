import random

num=random.randint(1,20)
print("I am thinking of a number between 1 and 20")

for i in range(1,7):

    print("Take a guess")
    a=int(input())

    if a> num:
        print("Guess is too high.")
    elif a<num:
        print("Guess is too low.")
    else:
        break;
    

if a==num:
    print("You guessed the number {} in {} tries.".format(num,i))
else:            
    print("The number is {}".format(num))
