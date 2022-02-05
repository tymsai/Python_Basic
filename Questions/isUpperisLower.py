#upper & lower
countL=countU=0
str="sasjdhASJDfhgSJpKsjhsk Js"
for i in range (len(str)):
    if(str[i].isupper()):
        countU+=1
    else:
        countL+=1
print(countU)
print(countL)
