import random
Number=int(input("Enter the number "))
a=0
b=100
i=0
while True:
    i=i+1
    rand=random.randint(a,b)
    if(rand==Number):
        print("Guessed at %d guess"%(i))
        break
    elif(rand>Number):
        b=rand
    elif(rand<Number):
        a=rand

        
