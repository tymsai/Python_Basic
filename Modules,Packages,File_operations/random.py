import random
#print(help(random))
def randomprices():
    possiblePrices=[]
    price=1
    while price<=10:
        price+=1
        possiblePrices.append(price)
    return random.sample(possiblePrices, 9)

print(randomprices())
