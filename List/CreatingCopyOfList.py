a=[1, 2, 3, 4, 5, 6]
b=a
c=list(a)
a[2]=99
print("without typecast - ", b)
print("with typecast (actual copy) - ", c)
