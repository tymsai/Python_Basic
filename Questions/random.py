import random
var=random.randint(0, 9)
print("The generated number is ", var)
print("Enter the same number ")
usr=int(input())
if(usr==var):
    print("Correct")
else:
    print("The no didnt match")
