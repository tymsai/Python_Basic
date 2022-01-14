#With type casting
print("Enter the number to print table upto 10")
user=int(input())
i=1
while(i<11):
    print(str(user)+"*"+str(i)+"="+str(user*i))
    i=i+1
    
#Without type casting
print("Enter the number to print table upto 10")
user=int(input())
i=1
while(i<11):
    print(user, "*", i, "=", user*i)
    i=i+1
