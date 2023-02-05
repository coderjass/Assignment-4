import random
count=0
while count<10 :
    a=random.randint(0,9)
    b=random.randint(0,9)
    print("Find product of numbers", a, b)
    prod=int(input("Your answer is: "))
    if prod==a*b:
        print("Right")
    else:
        print("Wrong, the answer is", a*b)
    count+=1
