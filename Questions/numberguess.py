import random
var=random.randint(0, 9)
print("A random number is generated b/w 0-9 ")
while(True):
    usr=int(input("Guess the number"))
    if(usr==var):
        print("Correct Guess")
        break;
    elif(usr>var):
        print("Try a lower number")
    else:
        print("Try a greater number")
    
