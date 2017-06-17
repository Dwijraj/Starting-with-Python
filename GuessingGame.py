import random
Gen=random.randint(0,100)
while(True):
    data=input("Enter your guess")
    if(int(data)==Gen):
        print("Correct Guess")
        break
    elif(int(data)<Gen):
        print("Guess Higher")
    else:
        print("Guess Lower")

        
    
